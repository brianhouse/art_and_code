#!/bin/bash

ffmpeg -f image2 -framerate 30 -i $1/screen-%04d.jpg output.gif
rm $1/*.jpg

# output=$(basename $1 .mov)
# output="${output}.gif"
#
# # ffmpeg -i $1 -vf "fps=24,scale=-1:720:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 $output
#
# palette="/tmp/palette.png"
# filters="fps=24,scale=-1:300:flags=lanczos"
#
# ffmpeg -i $1 -vf "$filters,palettegen" -y $palette
# ffmpeg -i $1 -i $palette -lavfi "$filters [x]; [x][1:v] paletteuse" -y $output
