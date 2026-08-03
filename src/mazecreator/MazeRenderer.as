// Maze rendering for the rebuilt mazeCreator (M2). Geometry + palette
// measured from archive/ia-items/extracted/images/"Making a maze.png"
// at uniform scale 832/688 = 1.2093 (docs/mazecreator-visual-spec.md).
// Wire semantics per MazeData: wall bits draw where stored; the
// unstorable south/east closure edges (floor at grid bottom/right edge)
// derive from floor adjacency. Floor tones are NOT a checkerboard in the
// evidence -- per-cell mix, ~1/3 light, rule unknowable -- so a
// deterministic hash stands in (identical across runtimes for gate C).
// Icons drawn axis-aligned with manual concentric-alpha glows: the
// capture is too soft to pin rotation, and filter support differs
// between Ruffle and the projector.
class MazeRenderer {

    // Assigned in initConstants(), NOT as field initializers: MTASC's
    // static-initializer order across auto-included classes is not
    // dependable under the real Flash 8 player (statics read as
    // undefined -> NaN geometry -> empty render), while Ruffle happens
    // to initialize eagerly. Editor.main() calls initConstants() first.
    static var CELL:Number;
    static var LATTICE_X:Number;
    static var LATTICE_Y:Number;
    static var LATTICE_W:Number;
    static var LATTICE_H:Number;
    static var WALL_T:Number;
    static var COLOR_WALL:Number;
    static var COLOR_FLOOR_LIGHT:Number;
    static var COLOR_FLOOR_DARK:Number;
    static var COLOR_TANK_LINE:Number;
    static var COLOR_TANK_FILL:Number;
    static var COLOR_CRATE_FILL:Number;
    static var COLOR_CRATE_EDGE:Number;
    static var COLOR_CRATE_GLOW:Number;
    static var COLOR_TANK_GLOW:Number;

    static function initConstants():Void {
        CELL = 32;
        LATTICE_X = 56;
        LATTICE_Y = 50;
        LATTICE_W = 18;
        LATTICE_H = 10;
        WALL_T = 4;
        COLOR_WALL = 0x444444;
        COLOR_FLOOR_LIGHT = 0xEEEEEE;
        COLOR_FLOOR_DARK = 0xDDDDDD;
        COLOR_TANK_LINE = 0x5555BB;
        COLOR_TANK_FILL = 0xAFB4EE;   // core tone (175,180,238)
        COLOR_CRATE_FILL = 0xDBB755;  // core tone (219,183,85)
        COLOR_CRATE_EDGE = 0xAA8232;
        COLOR_CRATE_GLOW = 0xF0D060;
        COLOR_TANK_GLOW = 0x8890E8;
    }

    // exact centering offsets in CELLS -- half-cell when parity is odd,
    // exactly as the screenshot lands (spec: 13-wide -> 2.5, 8-tall -> 1)
    static function originFor(data:MazeData):Object {
        return { x: LATTICE_X + ((LATTICE_W - data.w) / 2) * CELL,
                 y: LATTICE_Y + ((LATTICE_H - data.h) / 2) * CELL };
    }

    // ~1/3 light, deterministic (see class comment)
    static function floorTone(x:Number, y:Number):Number {
        return ((x * 3 + y * 7) % 3 == 0) ? COLOR_FLOOR_LIGHT : COLOR_FLOOR_DARK;
    }

    // ox/oy = absolute stage px of the grid's top-left corner
    static function render(mc:MovieClip, data:MazeData, ox:Number, oy:Number):Void {
        mc.clear();
        var x:Number; var y:Number;
        for (x = 0; x < data.w; x++) {
            for (y = 0; y < data.h; y++) {
                if (data.floor[x][y] != 1) continue;
                mc.beginFill(floorTone(x, y));
                boxAt(mc, ox + x * CELL, oy + y * CELL, CELL, CELL);
                mc.endFill();
            }
        }
        // one fill per segment: overlapping rects inside a single fill
        // cancel under the even-odd rule (corner overlaps became gaps)
        for (x = 0; x < data.w; x++) {
            for (y = 0; y < data.h; y++) {
                if (data.wallNorth[x][y] == 1)
                    wallBox(mc, ox + x * CELL - WALL_T / 2, oy + y * CELL - WALL_T / 2,
                            CELL + WALL_T, WALL_T);
                if (data.wallWest[x][y] == 1)
                    wallBox(mc, ox + x * CELL - WALL_T / 2, oy + y * CELL - WALL_T / 2,
                            WALL_T, CELL + WALL_T);
                if (data.floor[x][y] == 1 && (y == data.h - 1 || data.floor[x][y + 1] != 1))
                    wallBox(mc, ox + x * CELL - WALL_T / 2, oy + (y + 1) * CELL - WALL_T / 2,
                            CELL + WALL_T, WALL_T);
                if (data.floor[x][y] == 1 && (x == data.w - 1 || data.floor[x + 1][y] != 1))
                    wallBox(mc, ox + (x + 1) * CELL - WALL_T / 2, oy + y * CELL - WALL_T / 2,
                            WALL_T, CELL + WALL_T);
            }
        }
        for (var o:Number = 0; o < data.objects.length; o++) {
            var ob:Object = data.objects[o];
            var cx:Number = ox + (ob.x - 1) * CELL + CELL / 2;
            var cy:Number = oy + (ob.y - 1) * CELL + CELL / 2;
            if (ob.type == 8) drawCrate(mc, cx, cy);
            else drawTank(mc, cx, cy);
        }
    }

    static function wallBox(mc:MovieClip, x:Number, y:Number, w:Number, h:Number):Void {
        mc.beginFill(COLOR_WALL);
        boxAt(mc, x, y, w, h);
        mc.endFill();
    }

    static function boxAt(mc:MovieClip, x:Number, y:Number, w:Number, h:Number):Void {
        mc.moveTo(x, y); mc.lineTo(x + w, y); mc.lineTo(x + w, y + h);
        mc.lineTo(x, y + h); mc.lineTo(x, y);
    }

    static function glow(mc:MovieClip, cx:Number, cy:Number, color:Number, r:Number):Void {
        var a:Array = [10, 16, 22];
        for (var i:Number = 0; i < a.length; i++) {
            var rr:Number = r - i * 3;
            mc.beginFill(color, a[i]);
            boxAt(mc, cx - rr, cy - rr, rr * 2, rr * 2);
            mc.endFill();
        }
    }

    // axis-aligned amber square ~16x16, darker border, soft glow
    static function drawCrate(mc:MovieClip, cx:Number, cy:Number):Void {
        glow(mc, cx, cy, COLOR_CRATE_GLOW, 14);
        mc.lineStyle(2, COLOR_CRATE_EDGE);
        mc.beginFill(COLOR_CRATE_FILL);
        boxAt(mc, cx - 8, cy - 8, 16, 16);
        mc.endFill();
        mc.lineStyle();
    }

    // top-view tank: hull + tracks + barrel, blue outline, soft glow
    static function drawTank(mc:MovieClip, cx:Number, cy:Number):Void {
        glow(mc, cx, cy, COLOR_TANK_GLOW, 14);
        mc.lineStyle(2, COLOR_TANK_LINE);
        mc.beginFill(COLOR_TANK_FILL);
        boxAt(mc, cx - 6, cy - 8, 12, 16);      // hull
        mc.endFill();
        mc.beginFill(COLOR_TANK_LINE);
        boxAt(mc, cx - 10, cy - 9, 3, 18);      // left track
        boxAt(mc, cx + 7, cy - 9, 3, 18);       // right track
        boxAt(mc, cx - 1, cy - 14, 2, 8);       // barrel
        mc.endFill();
        mc.lineStyle();
    }
}
