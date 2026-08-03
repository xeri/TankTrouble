#!/bin/sh
cd "$(dirname "$0")"
../../thirdparty/mtasc/mtasc.exe -version 8 -swf editor.swf -main -header 688:400:25 Editor.as
cp editor.swf ../../srv/includes/mazeCreator_v0.3.swf
