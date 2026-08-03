#!/bin/sh
# Builds spike.swf. Header: 688x400 @ 25fps -- stage from the O embed
# (srv/index.php:3617), fps from the O comment (srv/index.php:3637).
cd "$(dirname "$0")"
../../thirdparty/mtasc/mtasc.exe -version 8 -swf spike.swf -main -header 688:400:25 Spike.as
