// Maze d= grid model for the rebuilt mazeCreator (M2, phase 2).
// Parse mirrors the O reader:
//   archive/decompiled/CLASSIC_TankTrouble_v4.0/scripts/__Packages/
//   MazeDataFetcher.as lines 67-162 (bit peel order 4,2,1; y outer, x inner;
//   objects 1-indexed; one terminator field skipped).
// DIVERGENCE from the reader's storage, for bit-fidelity: bit 2 is kept on
// the cell that carries it (wallNorth[x][y] = wall on the north side of
// (x,y)). The reader re-homes it on the upper cell and silently DROPS row
// 0's bit into [x][-1] -- but every corpus grid (670/670) has bit-2 digits
// in row 0 (the arena's top boundary), so the writer emitted them and a
// byte-faithful emit must preserve them.
// Emit gate: oracle/editor-roundtrip/run_roundtrip.mjs, all corpus grids.

class MazeData {

    var w:Number;
    var h:Number;
    var floor:Array;       // [x][y] 0/1 -- bit 1
    var wallNorth:Array;   // [x][y] 0/1 -- bit 2: wall between (x,y-1) and (x,y)
    var wallWest:Array;    // [x][y] 0/1 -- bit 4: wall between (x-1,y) and (x,y)
    var objects:Array;     // {x, y, type, params} -- 1-indexed, params raw
    var reservedField:String;

    function MazeData() { clear(1, 1); }

    function clear(width:Number, height:Number):Void {
        w = width; h = height;
        reservedField = "0";
        objects = [];
        floor = []; wallNorth = []; wallWest = [];
        for (var x:Number = 0; x < w; x++) {
            floor[x] = []; wallNorth[x] = []; wallWest[x] = [];
            for (var y:Number = 0; y < h; y++) {
                floor[x][y] = 0; wallNorth[x][y] = 0; wallWest[x][y] = 0;
            }
        }
    }

    function parse(d:String):Boolean {
        var f:Array = d.split("#");
        var i:Number = 0;
        var width:Number = Number(f[i++]);
        var cells:String = f[i++];
        if (!(width >= 1) || cells.length % width != 0) return false;
        clear(width, cells.length / width);
        reservedField = f[i++];
        var k:Number = 0;
        for (var y:Number = 0; y < h; y++) {
            for (var x:Number = 0; x < w; x++) {
                var v:Number = Number(cells.charAt(k++));
                if (isNaN(v) || v > 7) return false;
                if (v / 4 >= 1) { wallWest[x][y] = 1; v %= 4; }
                if (v / 2 >= 1) { wallNorth[x][y] = 1; v %= 2; }
                if (v >= 1)     { floor[x][y] = 1; }
            }
        }
        var count:Number = Number(f[i++]);
        if (isNaN(count)) return false;
        objects = [];
        for (var o:Number = 0; o < count; o++) {
            objects.push({ x: Number(f[i++]), y: Number(f[i++]),
                           type: Number(f[i++]), params: String(f[i++]) });
        }
        // O reader: _loc10_ = _loc10_ + 1  -- skips one terminator field
        i++;
        return true;
    }

    function emit():String {
        var cells:String = "";
        for (var y:Number = 0; y < h; y++) {
            for (var x:Number = 0; x < w; x++) {
                var v:Number = 0;
                if (floor[x][y] == 1)     v += 1;
                if (wallNorth[x][y] == 1) v += 2;
                if (wallWest[x][y] == 1)  v += 4;
                cells += String(v);
            }
        }
        var out:String = w + "#" + cells + "#" + reservedField + "#" + objects.length + "#";
        for (var o:Number = 0; o < objects.length; o++) {
            var ob:Object = objects[o];
            out += ob.x + "#" + ob.y + "#" + ob.type + "#" + ob.params + "#";
        }
        return out + "#0#";
    }
}
