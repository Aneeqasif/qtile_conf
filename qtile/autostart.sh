#!/bin/bash
function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}


run /usr/lib/polkit-kde-authentication-agent-1 
# run feh --bg-fill ~/Pictures/walls/mywall.jpg &
run feh --bg-fill /home/aneeq/Pictures/wallhaven-mpwe29.png &
run albert &
run volumeicon
run nm-applet --no-agent &
run klipper
run blueberry-tray &
# run picom &
run picom -b --experimental-backends --backend glx &
xautolock -time 5 -locker 'i3lock-fancy-rapid 46 4' &
alttab -mk Super_L -w 1 -d 2  -bg "#263238" -frame "#00BCD4" -bw 2 -bc "#00BCD4" -font "xft:Inter Medium-10" -inact "#3f4863" &
# run cbatticon &
