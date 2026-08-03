// The rebuilt mazeCreator (M2). Contract is O evidence (srv/index.php:
// 3609-3753): inbound SetVariable fadeOut / newToolRequested /
// _root.saveRequested / _root.mazeName / _root.errorPanel.hide /
// previewLoaded; outbound getURL javascript show/hideMazeCreatorTools
// AndTitle. Dual channel per oracle/editor-spike verdicts: EI callback
// for Ruffle (names arrive literal, "_root." stripped), _root.watch +
// a real _root.errorPanel object for native SetVariable under the
// projector. Interaction model + initCode fields (u,n,t,d,s) are M3
// (DECISIONS 2026-08-03); visuals M2 per docs/mazecreator-visual-spec.md.
import flash.external.ExternalInterface;

class Editor {

    static var app:Editor;
    static function main() { app = new Editor(); }

    static var SAVE_ENDPOINT:String = "saveMaze.php"; // sibling of the SWF in includes/
    static var EDGE_TOL:Number = 6;

    var data:MazeData;          // full 18x10 editing lattice
    var state:String;           // "preview" | "edit"
    var tool:String;            // construct | crateSpawn | tankSpawn
    var title:String;
    var userId:String; var userName:String; var slot:String;
    var errorVisible:Boolean;
    var fadeTarget:Number;
    var fracX:Number; var fracY:Number;   // half-cell placement remainder, px

    var mazeMc:MovieClip; var panelMc:MovieClip;
    var titleTf:TextField; var panelTf:TextField;

    function Editor() {
        var init:Object = decodeInit(String(_root.initCode));
        userId = (init.u != undefined) ? String(init.u) : "";
        userName = (init.n != undefined) ? String(init.n) : "";
        title = (init.t != undefined) ? String(init.t) : "";
        slot = (init.s != undefined) ? String(init.s) : "1";

        data = new MazeData();
        data.clear(MazeRenderer.LATTICE_W, MazeRenderer.LATTICE_H);
        fracX = 0; fracY = 0;
        if (init.d != undefined && String(init.d) != "") loadIntoLattice(String(init.d));

        state = "preview";
        tool = "construct";
        errorVisible = false;

        buildStage();
        wireChannels();

        // page embeds us hidden and fades us in at +1200ms; standalone
        // projector has no page, so boot visible there.
        if (ExternalInterface.available) { _root._alpha = 0; fadeTarget = 0; }
        else { _root._alpha = 100; fadeTarget = 100; }
        var owner:Editor = this;
        _root.onEnterFrame = function() { owner.fadeStep(); };
        _root.onMouseDown = function() { owner.onClick(_root._xmouse, _root._ymouse); };
        redraw();
    }

    // ---- boot helpers -------------------------------------------------
    function decodeInit(code:String):Object {
        var o:Object = {};
        if (code == "undefined" || code == null || code == "") return o;
        // FlashVars/query transport can decode '+' to space; base64 never
        // legitimately contains spaces, so restore before decoding
        code = Base64.StringReplaceAll(code, " ", "+");
        var pairs:Array = Base64.Decode(code).split("&");
        for (var i:Number = 0; i < pairs.length; i++) {
            var kv:Array = pairs[i].split("=");
            o[kv[0]] = kv[1];
        }
        return o;
    }

    // place the boot maze centered on the lattice at exact (L-size)/2
    // offsets (spec rule): integer part into the lattice arrays, half-cell
    // remainder as a render/hit-test pixel shift
    function loadIntoLattice(d:String):Void {
        var m:MazeData = new MazeData();
        if (!m.parse(d)) return;
        var offX:Number = (MazeRenderer.LATTICE_W - m.w) / 2;
        var offY:Number = (MazeRenderer.LATTICE_H - m.h) / 2;
        var cx:Number = Math.floor(offX);
        var cy:Number = Math.floor(offY);
        fracX = (offX - cx) * MazeRenderer.CELL;
        fracY = (offY - cy) * MazeRenderer.CELL;
        for (var x:Number = 0; x < m.w; x++) {
            for (var y:Number = 0; y < m.h; y++) {
                data.floor[x + cx][y + cy] = m.floor[x][y];
                data.wallNorth[x + cx][y + cy] = m.wallNorth[x][y];
                data.wallWest[x + cx][y + cy] = m.wallWest[x][y];
            }
        }
        for (var o:Number = 0; o < m.objects.length; o++) {
            var ob:Object = m.objects[o];
            data.objects.push({ x: ob.x + cx, y: ob.y + cy,
                                type: ob.type, params: ob.params });
        }
        data.reservedField = m.reservedField;
        data.normalizeBoundary();
    }

    // crop the lattice back to the corpus shape: tight floor bbox,
    // boundary bits normalized (670/670 invariant)
    function cropToFloorBbox():MazeData {
        var x0:Number = 999; var x1:Number = -1; var y0:Number = 999; var y1:Number = -1;
        var x:Number; var y:Number;
        for (x = 0; x < data.w; x++)
            for (y = 0; y < data.h; y++)
                if (data.floor[x][y] == 1) {
                    if (x < x0) x0 = x; if (x > x1) x1 = x;
                    if (y < y0) y0 = y; if (y > y1) y1 = y;
                }
        var out:MazeData = new MazeData();
        if (x1 < 0) { out.clear(1, 1); return out; }
        out.clear(x1 - x0 + 1, y1 - y0 + 1);
        for (x = x0; x <= x1; x++)
            for (y = y0; y <= y1; y++) {
                out.floor[x - x0][y - y0] = data.floor[x][y];
                out.wallNorth[x - x0][y - y0] = data.wallNorth[x][y];
                out.wallWest[x - x0][y - y0] = data.wallWest[x][y];
            }
        for (var o:Number = 0; o < data.objects.length; o++) {
            var ob:Object = data.objects[o];
            out.objects.push({ x: ob.x - x0, y: ob.y - y0, type: ob.type, params: ob.params });
        }
        out.normalizeBoundary();
        return out;
    }

    // ---- control channels ---------------------------------------------
    function wireChannels():Void {
        var owner:Editor = this;
        ExternalInterface.addCallback("SetVariable", null,
            function(n:String, v:String) { owner.onSetVariable(n, v); });
        ExternalInterface.addCallback("GetVariable", null,
            function(n:String):String { return owner.getVar(n); });
        var names:Array = ["newToolRequested", "saveRequested", "mazeName",
                           "previewLoaded", "fadeOut"];
        for (var i:Number = 0; i < names.length; i++) {
            _root.watch(names[i], function(prop, oldVal, newVal) {
                owner.onSetVariable(String(prop), String(newVal)); return newVal;
            });
        }
        _root.errorPanel = { hide: "" };
        _root.errorPanel.watch("hide", function(prop, oldVal, newVal) {
            owner.onSetVariable("errorPanel.hide", String(newVal)); return newVal;
        });
    }

    function onSetVariable(name:String, value:String):Void {
        if (name.substr(0, 6) == "_root.") name = name.substr(6);
        // transport artifact: Ruffle's SetVariable turns "" into null and
        // the watch channel stringifies it -- normalize back to ""
        if (value == null || value == "null" || value == "undefined") value = "";
        if (name == "fadeOut") fadeTarget = (value == "true") ? 0 : 100;
        else if (name == "newToolRequested") {
            if (value == "construct" || value == "crateSpawn" || value == "tankSpawn")
                tool = value;
        }
        else if (name == "mazeName") { title = value; hideError(); redraw(); }
        else if (name == "errorPanel.hide") { if (value == "yes") hideError(); }
        else if (name == "previewLoaded") { state = "preview"; redraw(); }
        else if (name == "saveRequested") { if (value == "true") doSave(); }
    }

    function getVar(name:String):String {
        if (name == "mazeD") return cropToFloorBbox().emit();
        if (name == "state") return state;
        if (name == "tool") return tool;
        if (name == "titleText") return title;
        if (name == "errorVisible") return errorVisible ? "true" : "false";
        if (name == "errorText") return panelTf.text;
        if (name == "stageAlpha") return String(Math.round(_root._alpha));
        return "";
    }

    // ---- interaction ---------------------------------------------------
    function onClick(mx:Number, my:Number):Void {
        if (_root._alpha < 50) return;
        if (state == "preview") {
            state = "edit";
            getURL("javascript:showMazeCreatorToolsAndTitle('" + userId + "','"
                   + title + "')");
            redraw();
            return;
        }
        var lx:Number = mx - MazeRenderer.LATTICE_X - fracX;
        var ly:Number = my - MazeRenderer.LATTICE_Y - fracY;
        var C:Number = MazeRenderer.CELL;
        if (lx < -EDGE_TOL || ly < -EDGE_TOL) return;
        var cx:Number = Math.floor(lx / C);
        var cy:Number = Math.floor(ly / C);
        if (cx < 0 || cy < 0 || cx >= data.w || cy >= data.h) return;
        if (tool == "construct") {
            var dx:Number = lx - cx * C;   // 0..C within the cell
            var dy:Number = ly - cy * C;
            // near an interior gridline between two floor cells -> wall
            if (dx < EDGE_TOL && cx > 0
                && data.floor[cx][cy] == 1 && data.floor[cx - 1][cy] == 1)
                data.wallWest[cx][cy] = 1 - data.wallWest[cx][cy];
            else if (dx > C - EDGE_TOL && cx < data.w - 1
                && data.floor[cx][cy] == 1 && data.floor[cx + 1][cy] == 1)
                data.wallWest[cx + 1][cy] = 1 - data.wallWest[cx + 1][cy];
            else if (dy < EDGE_TOL && cy > 0
                && data.floor[cx][cy] == 1 && data.floor[cx][cy - 1] == 1)
                data.wallNorth[cx][cy] = 1 - data.wallNorth[cx][cy];
            else if (dy > C - EDGE_TOL && cy < data.h - 1
                && data.floor[cx][cy] == 1 && data.floor[cx][cy + 1] == 1)
                data.wallNorth[cx][cy + 1] = 1 - data.wallNorth[cx][cy + 1];
            else {
                data.floor[cx][cy] = 1 - data.floor[cx][cy];
                if (data.floor[cx][cy] == 0) removeObjectAt(cx + 1, cy + 1);
                data.normalizeBoundary();
            }
        } else {
            if (data.floor[cx][cy] != 1) return;
            var t:Number = (tool == "tankSpawn") ? 5 : 8;
            if (!removeObjectAt(cx + 1, cy + 1)) {
                var tanks:Number = 0; var crates:Number = 0;
                for (var i:Number = 0; i < data.objects.length; i++) {
                    if (data.objects[i].type == 5) tanks++; else crates++;
                }
                if (data.objects.length >= 10) return;
                if (t == 5 && tanks >= 5) return;
                if (t == 8 && crates >= 5) return;
                data.objects.push({ x: cx + 1, y: cy + 1, type: t, params: "" });
            }
        }
        redraw();
    }

    function removeObjectAt(x1:Number, y1:Number):Boolean {
        for (var i:Number = 0; i < data.objects.length; i++) {
            if (data.objects[i].x == x1 && data.objects[i].y == y1) {
                data.objects.splice(i, 1); return true;
            }
        }
        return false;
    }

    // ---- save ------------------------------------------------------------
    function doSave():Void {
        if (state != "edit") return;
        if (!validTitle(title)) { showError("Please give your maze a name."); return; }
        var inner:String = "t=" + title + "&n=" + userName + "&d="
                         + cropToFloorBbox().emit() + "&s=" + slot;
        var post:LoadVars = new LoadVars();
        post.q = Base64.Encode(inner);
        var reply:LoadVars = new LoadVars();
        var owner:Editor = this;
        reply.onLoad = function(ok:Boolean) {
            if (!ok) { owner.showError("Could not reach the server."); return; }
            // body is r=<base64>; LoadVars url-decodes it, turning '+'
            // into space -- restore before decoding
            var raw:String = Base64.StringReplaceAll(String(this.r), " ", "+");
            var pairs:Array = Base64.Decode(raw).split("&");
            var res:Object = {};
            for (var i:Number = 0; i < pairs.length; i++) {
                var kv:Array = pairs[i].split("=");
                res[kv[0]] = kv[1];
            }
            if (res.saved == "true") {
                owner.hideError();
                owner.state = "preview";
                owner.redraw();
                getURL("javascript:hideMazeCreatorToolsAndTitle('" + owner.userId + "')");
            } else {
                owner.showError(owner.errorCopy(String(res.error)));
            }
        };
        post.sendAndLoad(SAVE_ENDPOINT, reply, "POST");
    }

    // M3 copy -- the original panel text is unrecorded (known only from
    // _root.errorPanel.hide; VISUAL-EVIDENCE-WANTED #2). Codes are the
    // invented saveMaze.php set.
    function errorCopy(code:String):String {
        if (code == "badTitle") return "Please give your maze a name.";
        if (code == "tooManyObjects") return "Too many spawn points.";
        return "Your maze could not be saved.";
    }

    function validTitle(t:String):Boolean {
        if (t == null || t.length < 1 || t.length > 32) return false;
        var legal:String = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                         + "abcdefghijklmnopqrstuvwxyz !,-.?";
        for (var i:Number = 0; i < t.length; i++)
            if (legal.indexOf(t.charAt(i)) < 0) return false;
        return true;
    }

    // ---- display ---------------------------------------------------------
    function buildStage():Void {
        var bg:MovieClip = _root.createEmptyMovieClip("bg", 1);
        bg.beginFill(0xFFFFFF);
        bg.moveTo(0, 0); bg.lineTo(688, 0); bg.lineTo(688, 400); bg.lineTo(0, 400);
        bg.endFill();
        mazeMc = _root.createEmptyMovieClip("maze", 2);

        // title band: stage y ~10-22, #666666, centered (visual spec)
        _root.createTextField("titleTf", 3, 0, 6, 688, 26);
        titleTf = _root.titleTf;
        var tfm:TextFormat = new TextFormat();
        tfm.font = "_sans"; tfm.size = 18; tfm.color = 0x666666; tfm.align = "center";
        titleTf.setNewTextFormat(tfm); titleTf.selectable = false;

        // watermark: right-aligned to x~682, bottom edge, letter-spaced
        _root.createTextField("versionTf", 4, 482, 380, 200, 18);
        var vf:TextFormat = new TextFormat();
        vf.font = "_sans"; vf.size = 12; vf.color = 0xBBBBBB; vf.align = "right";
        vf.letterSpacing = 2;
        _root.versionTf.setNewTextFormat(vf);
        _root.versionTf.selectable = false;
        _root.versionTf.text = "version 0.3";

        // error panel: M3 -- never captured (VISUAL-EVIDENCE-WANTED #2)
        panelMc = _root.createEmptyMovieClip("panel", 5);
        panelMc.beginFill(0x444444, 90);
        panelMc.moveTo(144, 160); panelMc.lineTo(544, 160);
        panelMc.lineTo(544, 240); panelMc.lineTo(144, 240);
        panelMc.endFill();
        panelMc.createTextField("msg", 1, 154, 185, 380, 40);
        panelTf = panelMc.msg;
        var pf:TextFormat = new TextFormat();
        pf.font = "_sans"; pf.size = 14; pf.color = 0xFFFFFF; pf.align = "center";
        panelTf.setNewTextFormat(pf); panelTf.selectable = false;
        panelMc._visible = false;
    }

    function redraw():Void {
        MazeRenderer.render(mazeMc, data,
            MazeRenderer.LATTICE_X + fracX, MazeRenderer.LATTICE_Y + fracY);
        titleTf.text = title;
    }

    function showError(msg:String):Void {
        panelTf.text = msg; panelMc._visible = true; errorVisible = true;
    }
    function hideError():Void { panelMc._visible = false; errorVisible = false; }

    function fadeStep():Void {
        var step:Number = 100 / 15;   // 15 frames @ 25fps (srv/index.php:3637)
        if (_root._alpha < fadeTarget) _root._alpha = Math.min(fadeTarget, _root._alpha + step);
        else if (_root._alpha > fadeTarget) _root._alpha = Math.max(fadeTarget, _root._alpha - step);
    }
}
