#!/bin/bash

output=$(basename $1 .mov)
output="${output}.gif"

ffmpeg -i $1 -vf "fps=30,scale=320:-1:flags=lanczos,split[s0][s1];[s0]palettegen[p];[s1][p]paletteuse" -loop 0 $output
