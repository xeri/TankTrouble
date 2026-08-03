// Projector diagnostic (never ships): encodes boot pipeline state as
// horizontal bar widths readable from a screenshot.
//   y=0   blue   : String(_root.initCode).length px (b64 in, expect 300)
//   y=20  green  : Base64-decoded length px (expect 223)
//   y=40  orange : pairs decoded x 20 px (expect 5 -> 100)
//   y=60  d len  : purple, length of init.d px (expect 183)
//   y=80  parse  : green 200px if MazeData.parse(d) true, red 200px if false
//   y=100 width  : dark, data.w x 10 px (expect 130)
//   y=150 render : MazeRenderer.render of the parsed maze
class Diag {
    static function main() {
        MazeRenderer.initConstants();
        var mc:MovieClip = _root.createEmptyMovieClip("diag", 1);
        var code:String = String(_root.initCode);
        bar(mc, 0, 0x3366CC, code.length);

        code = Base64.StringReplaceAll(code, " ", "+");
        var decoded:String = Base64.Decode(code);
        bar(mc, 20, 0x33CC66, decoded.length);

        var o:Object = {};
        var pairs:Array = decoded.split("&");
        for (var i:Number = 0; i < pairs.length; i++) {
            var kv:Array = pairs[i].split("=");
            o[kv[0]] = kv[1];
        }
        bar(mc, 40, 0xCC8833, pairs.length * 20);

        var d:String = (o.d != undefined) ? String(o.d) : "";
        bar(mc, 60, 0x9933CC, d.length);

        var m:MazeData = new MazeData();
        var ok:Boolean = m.parse(d);
        bar(mc, 80, ok ? 0x33CC33 : 0xCC3333, 200);

        bar(mc, 100, 0x444444, m.w * 10);

        var maze:MovieClip = _root.createEmptyMovieClip("maze", 2);
        var org:Object = MazeRenderer.originFor(m);
        MazeRenderer.render(maze, m, org.x, 150 + (org.y - 150) * 0);
    }
    static function bar(mc:MovieClip, y:Number, rgb:Number, w:Number):Void {
        if (!(w > 0)) return;
        mc.beginFill(rgb);
        mc.moveTo(0, y); mc.lineTo(w, y); mc.lineTo(w, y + 16);
        mc.lineTo(0, y + 16); mc.lineTo(0, y);
        mc.endFill();
    }
}
