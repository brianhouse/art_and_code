# Python Mode for Processing Cheat Sheet

Arguments to functions can be numbers or variables, and the variables can be named anything—the order is what matters. Below, the arguments are named descriptively in order to explain how the function works.

### Canvas
- `size(width, height)` set canvas size in pixels
- `background(color)` set window background color
- `pixelDensity(2)` make all lines smoother on some displays


### Shapes
- `point(x, y)`
- `line(x1, y1, x2, y2)`
- `circle(x, y, diameter)` (drawn from center)
- `ellipse(x, y, width, height)` (drawn from center)
- `triangle(x1, y1, x2, y2, x3, y3)`
- `square(x, y, width)` (drawn from upper-left corner)
- `rect(x, y, width, height)` (drawn from upper-left corner)
- `quad(x1, y1, x2, y2, x3, y3, x4, y4)`
- `bezier(x_start, y_start, x_anchor1, y_anchor1, x_anchor2, y_anchor2, x_stop, y_stop)`
- ```beginShape()``` start a curve shape
- ```curveVertex(x, y)``` add an anchor point
- ```endShape()``` end the shape



### Stroke + Color
- `stroke(color)`
- `fill(color)`
- `strokeWeight(pixels)`


### Color Values
- `fill(100)` 1 argument is greyscale
- `fill(100, 50)` 2 arguments is greyscale + opacity
- `fill(100, 200, 0)` 3 arguments is color
- `fill(100, 200, 0, 50)` 4 arguments is color + opacity


### Structure
- `for i in range(n):` repeat the following indented lines _n_ times, with `i` equal to _n_ each time
- `def function_name():` declare a function with the following indented lines
- `if` `elif` `else` create a conditional statement
- `and` `or` combine conditions in an `if` statement


### Strings
- `string.lower()` return a lowercase version of the string
- `string.upper()` return an uppercase version of the string
- `string.replace("search", "replace")` return a version of the string with the substring "search" replaced with "replace"
- `string.split()` split a string on any whitespace and create a list
- `string.split(string)` split a string on any arbitrary substring and create a list
- `string.splitlines()` split a string on any newline character
- `" ".join(list)` join a list with a space (or other character) between each list item
- `len(string)` get the number of characters in a string
- `in` test whether a string is within another string or a list


### Lists
- `my_list = []` create an empty list
- `my_list = [item1, item2, item3]` create a list with items
- `list.append(item)` append an item to a list
- `list.remove(item)` remove an item from a list
- `list[index]` return the item at _index_ from the list
- `len(list)` get the length of the list
- `in` test whether an item is within the list
- `words = list(set(words))` convert a list with repeats into a list with only unique items


### Dictionaries
- `my_dictionary = {}` create an empty dictionary
- `my_dictionary = {'name': "Brian", 'hobby': "skiing"}` create a dictionary with items
- `my_dictionary['name']` access a dictionary item
- `my_dictionary['skill'] = "programming"` add an item to a dictionary


### Random
- `random(low, high)` generates a number greater than or equal to _low_ and less than _high_
- `random(high)` generates a number greater than or equal to 0 less than _high_
- `randomGaussian()` generates a number from a series with a mean of 0 and a standard deviation of 1
- `choice(list)` select a random item from a list (requires `from random import choice`)
- `shuffle(list)` shuffle a list in place


### Event handlers
- `setup()` called once when the sketch is first run
- `draw()` called repeatedly 30 times per second
- `mouseClicked()` called with the mouse is pressed and released in the same location
- `keyTyped()` called when a key is typed


### Magic variables
- `mouseX` the current x-coordinate of the cursor
- `mousey` the current y-coordinate of the cursor
- `pmouseX` the previous x-coordinate of the cursor
- `pmouseY` the previous y-coordinate of the cursor
- `mousePressed` whether the mouse button is pressed or not (`True`/`False`)
- `key` the most recently typed key
- `width` the width of the canvas
- `height` the height of the canvas


### Comparison operators
- `==` equal to
- `>` greater than
- `<` lesser than
- `>=` greater than or equal to
- `<=` lesser than or equal to
- `!=` not equal to


### Images
- `image = loadImage("image.png")` load data from an image file into a variable
- `pixel = image.get(x, y)` get color data for a single pixel
- `r = red(pixel)` get the red value of a pixel
- `g = green(pixel)` get the blue value of a pixel
`- b = blue(pixel)` get the green value of a pixel


### Utilities
- `global` declare a global variable
- `open("filename").read()` read the contents of a file into a string
- `save("filename.png")` save an image of the canvas
- `print("text")` print a string to the console
- `string = raw_input()` get a string from the command prompt and put it into a variable (only works in terminal)


## Full Documentation
https://py.processing.org/reference/
