// Editor control-channel spike (guide 6.5 pre-work; plan
// docs/superpowers/plans/2026-08-03-mazecreator-phase1-spike.md Task 2).
// Exercises every channel the rebuilt mazeCreator needs:
//   FlashVars in, ExternalInterface callback in, _root-variable semantics,
//   getURL("javascript:") out, and code-drawn vector output.
// NOT part of srv/ — oracle tooling, no provenance tier.

import flash.external.ExternalInterface;

class Spike {

    static var app:Spike;
    static function main() { app = new Spike(); }

    var lastSet:String;
    var initDecoded:String;

    function Spike() {
        lastSet = "";
        initDecoded = decode64(String(_root.initCode));

        paint(0x336699);

        // Channel A: classic plugin API name, re-exposed via ExternalInterface.
        // Under real Flash the native SetVariable exists and addCallback of the
        // same name may be ignored -- both routes land in onSetVariable via the
        // _root watch below, so behaviour converges.
        var owner:Spike = this;
        ExternalInterface.addCallback("SetVariable", null,
            function(n:String, v:String) { owner.onSetVariable(n, v); });
        ExternalInterface.addCallback("GetVariable", null,
            function(n:String):String { return String(owner[n]); });

        // Channel B: native SetVariable writes _root vars directly; watch them.
        // Covers real-Flash/projector, where addCallback("SetVariable") may lose
        // to the built-in method.
        _root.watch("newToolRequested",
            function(prop, oldVal, newVal) { owner.onSetVariable(String(prop), String(newVal)); return newVal; });
        _root.watch("saveRequested",
            function(prop, oldVal, newVal) { owner.onSetVariable(String(prop), String(newVal)); return newVal; });

        // Channel C: SWF -> page, already proven for ORIGINAL bytes; this
        // proves it for MTASC-built bytes too.
        getURL("javascript:__spikeBoot('" + initDecoded + "')");
    }

    function onSetVariable(n:String, v:String):Void {
        lastSet = n + "=" + v;
        if (n == "newToolRequested") {
            if (v == "construct")  paint(0x33cc33);
            if (v == "crateSpawn") paint(0xcc8833);
            if (v == "tankSpawn")  paint(0xcc3333);
        }
        if ((n == "saveRequested" || n == "_root.saveRequested") && v == "true") {
            getURL("javascript:__spikeSaved('" + lastSet + "')");
        }
    }

    function paint(rgb:Number):Void {
        var c:MovieClip = _root.createEmptyMovieClip("canvas", 1);
        c.beginFill(rgb);
        c.moveTo(0, 0); c.lineTo(688, 0); c.lineTo(688, 400); c.lineTo(0, 400);
        c.endFill();
    }

    // Minimal Base64 -- the era client ships its own __Packages.Base64; the
    // spike only needs decode of [A-Za-z0-9+/=].
    function decode64(s:String):String {
        if (s == "undefined" || s == null || s == "") return "";
        var tab:String = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
        var out:String = ""; var buf:Number = 0; var bits:Number = 0;
        for (var i:Number = 0; i < s.length; i++) {
            var v:Number = tab.indexOf(s.charAt(i));
            if (v < 0) continue;
            buf = (buf << 6) | v; bits += 6;
            if (bits >= 8) { bits -= 8; out += String.fromCharCode((buf >> bits) & 0xff); }
        }
        return out;
    }
}
