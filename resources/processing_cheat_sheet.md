# Python Mode for Processing Cheat Sheet

## Canvas
- `size(width, height)` set canvas size in pixels
- `background(color)` set window background color
- `pixelDensity(2)` make all lines smoother on nicer displays


## Shapes
- `point(x, y)`
- `line(x1, y1, x2, y2)`
- `circle(x, y, diameter)` (drawn from center)
- `ellipse(x, y, width, height)` (drawn from center)
- `triangle(x1, y1, x2, y2, x3, y3)`
- `square(x, y, width)` (drawn from upper-left corner)
- `rect(x, y, width, height)` (drawn from upper-left corner)
- `quad(x1, y1, x2, y2, x3, y3, x4, y4)`
- `bezier(x_start, y_start, x_anchor1, y_anchor1, x_anchor2, y_anchor2, x_stop, y_stop)`

## Stroke + Color
- `stroke(color)`
- `fill(color)`
- `strokeWeight(pixels)`

## Color Values
- `fill(100)` 1 parameter is greyscale
- `fill(100, 50)` 2 parameters is greyscale + opacity
- `fill(100, 200, 0)` 3 parameters is color
- `fill(100, 200, 0, 50)` 4 parameters is color + opacity


## Other
- `save("filename.png")`
- `print("text")`

## Full Documentation
https://py.processing.org/reference/
