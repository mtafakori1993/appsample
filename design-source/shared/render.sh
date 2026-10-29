#!/bin/bash
# usage: render.sh name  -> out/name.png (1600x1200)
cd "$(dirname "$0")"
google-chrome --headless=new --no-sandbox --disable-gpu --hide-scrollbars --force-device-scale-factor=1 --window-size=1600,1200 --virtual-time-budget=4000 --screenshot=out/$1.png file://$PWD/$1.html >/dev/null 2>&1
echo rendered $1
