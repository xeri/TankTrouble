#!/bin/sh
cd "$(dirname "$0")"
../../thirdparty/mtasc/mtasc.exe -version 8 -cp ../../src/mazecreator -swf harness.swf -main -header 688:400:25 TestHarness.as
