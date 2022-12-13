#!/bin/bash

picom -b 
source ~/.screenlayout/default.sh
nitrogen --restore
setxkbmap -option ctrl:nocaps &
amixer sseid Master 100%
