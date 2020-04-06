#!/bin/bash

output=$(basename $1 .mov)
output="${output}.gif"

# ffmpeg -i $1 -vf "fps=24,scale=-1:720:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 $output

palette="/tmp/palette.png"
filters="fps=24,scale=-1:720:flags=lanczos"

ffmpeg -i $1 -vf "$filters,palettegen" -y $palette
ffmpeg -i $1 -i $palette -lavfi "$filters [x]; [x][1:v] paletteuse" -y $output
