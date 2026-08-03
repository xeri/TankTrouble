// Visual gate harness (phase 3). Renders an arbitrary d= via EI for
// run_visual.mjs screenshots. Never ships.
import flash.external.ExternalInterface;

class RenderHarness {
    static function main() {
        MazeRenderer.initConstants();
        var bg:MovieClip = _root.createEmptyMovieClip("bg", 1);
        bg.beginFill(0xFFFFFF);
        bg.moveTo(0, 0); bg.lineTo(688, 0); bg.lineTo(688, 400); bg.lineTo(0, 400);
        bg.endFill();
        var maze:MovieClip = _root.createEmptyMovieClip("maze", 2);
        ExternalInterface.addCallback("renderMaze", null, function(d:String):String {
            var m:MazeData = new MazeData();
            if (!m.parse(d)) return "PARSE-FAIL";
            var org:Object = MazeRenderer.originFor(m);
            MazeRenderer.render(maze, m, org.x, org.y);
            return "ok";
        });
    }
}
