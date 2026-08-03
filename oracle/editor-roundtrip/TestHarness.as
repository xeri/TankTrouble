// Round-trip gate harness (phase 2). Exposes MazeData.parse->emit via
// ExternalInterface for run_roundtrip.mjs. Test scaffolding only -- this
// class never ships in the editor SWF.
import flash.external.ExternalInterface;

class TestHarness {
    static function main() {
        ExternalInterface.addCallback("roundTrip", null, function(d:String):String {
            var m:MazeData = new MazeData();
            if (!m.parse(d)) return "PARSE-FAIL";
            return m.emit();
        });
        // boundary-bit law (DECISIONS 2026-08-03): normalize must be a
        // no-op on every corpus grid
        ExternalInterface.addCallback("roundTripNormalized", null, function(d:String):String {
            var m:MazeData = new MazeData();
            if (!m.parse(d)) return "PARSE-FAIL";
            m.normalizeBoundary();
            return m.emit();
        });
        // visible liveness marker
        var c:MovieClip = _root.createEmptyMovieClip("bg", 1);
        c.beginFill(0x224422);
        c.moveTo(0, 0); c.lineTo(688, 0); c.lineTo(688, 400); c.lineTo(0, 400);
        c.endFill();
    }
}
