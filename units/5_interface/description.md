# Sketch #5: Expressive Interface

When we interact with a computer, we do so through a software interface. The files and folders of the operating system, the prompt of a text-based terminal, the links of a webpage, and the tool palette and working space of a graphics program—in all of these examples, input from the keyboard and mouse are translated into meaningful actions. Though we take many interfaces for granted, interfaces reflect the biases of those who made them. Furthermore, designing an interface is a creative act unto itself, and one that is central to digital media artists who use code to build their own tools.

For this sketch, you will create a software painting interface using p5. To get started, think about programs like [MacPaint](https://en.wikipedia.org/wiki/MacPaint), where the "user" can choose from multiple brushes with the mouse and use them to draw on the open canvas. However, your approach should reflect your own artistic theme. For example:
- an interface with a [street-art aesthetic](https://www.google.com/search?q=graffiti) and spray-paint brushes
- an interface from the "[future](https://www.google.com/search?q=future+interface)"    
- an interface for someone who is [color blind](https://en.wikipedia.org/wiki/Color_blindness), a [bird](https://en.wikipedia.org/wiki/Bird_vision#Light_perception), [underwater](http://thedivingblog.com/colors-underwater/) or who otherwise sees the world in ways not typically accounted for in interfaces

Requirements:
- Your interface must include at least 5 different "brushes" / ways of interacting
- It should be presented on a webpage that includes your title and [3-sentence description](../../resources/description_guidelines.md)
- Your page should also include an example image of an artwork that you have made with your interface
- This page should be hosted on GitHub and linked to from your portfolio

Note that this assignment will have a preliminary crit—please have your work posted online prior.


## Technical Resources

#### Textbook

Please read Chapter 5: "Response" (page 59) of _Getting Started with p5.js_ for this assignment, which explains how to incorporate user input. Chapter 4: "Variables" (page 41) will also be helpful.


#### p5js.org

For this assignment, see the "Mouse" and "Keyboard" functions at https://p5js.org/reference/  

Additional input examples:
- [Mouse Press](https://p5js.org/examples/input-mouse-press.html)
- [Mouse Functions (draggable object)](https://p5js.org/examples/input-mouse-functions.html)
- [Keyboard Input](https://p5js.org/examples/input-keyboard.html)
- [Changing the Cursor](https://p5js.org/reference/#/p5/cursor)

Important new p5 functions:
- [`random()`](https://p5js.org/reference/#/p5/random)


#### Shiffman

Draw function, variables, and the mouse:
https://www.youtube.com/watch?v=RnS0YNuLfQQ

Variables in general:
https://www.youtube.com/watch?v=Bn_B3T_Vbxs

The random function:
https://www.youtube.com/watch?v=nfmV2kuQKwA

If-statements with number comparisons:
https://www.youtube.com/watch?v=1Osb_iGDdjk


## Preparation

Similar to last assignment, you will create a new folder called `interface` on your computer and a corresponding repository on GitHub. These will contain an `index.html` file that looks like this:

```html
<html>
  <head>
    <title>Expressive Interface</title>
    <script src="https://cdn.jsdelivr.net/npm/p5@0.10.2/lib/p5.js"></script>
    <script src="sketch.js"></script>
  </head>
  <body>
      <h1>A title</h1>
      <p>A description</p>
      <!-- <img src="example.jpg" height="400" style="float: right;"/> -->      
      <div id="p5"></div>
  </body>
</html>
```

...and a `sketch.js` file that looks like this:

```js
function setup() {

    // create a 640x480 pixel canvas and attach it to your HTML
    createCanvas(640, 480).parent('p5')

}

function draw() {

    background(200)

}

function mouseClicked() {

    print(int(mouseX), int(mouseY))

}
```



## Example Code


#### Interface Elements

The following `draw()` and `mouseClicked()` functions work together to make a basic interface:

```js
// declare a variable to keep track of what brush we're using and it's color
let brush
let brush_color

function setup() {

    createCanvas(640, 480).parent('p5')
    background(200)

    // set default values here
    brush = "pencil"
    brush_color = color(255, 0, 0)  // set the initial brush color here

}

function draw() {

    if (mouseIsPressed) {
        cursor(CROSS)   // change the cursor to a cross while drawing

        if (brush == "pencil") {
            stroke(brush_color)
            strokeWeight(1)
            line(pmouseX, pmouseY, mouseX, mouseY) // draw a line from the previous mouse position to the current mouse position
        }

        if (brush == "dribbles") {
            fill(brush_color)
            noStroke()
            circle(mouseX, mouseY, random(2, 30))
        }

    } else {
        cursor(ARROW)   // change the cursor back to normal
    }

    stroke(0)
    strokeWeight(1)

    // make the toolbar area
    fill(100)
    rect(0, 0, 50, height)  // magic variable "height" is the canvas height

    // make the red button
    fill(255, 0, 0)
    rect(10, 10, 30, 30)

    // make the blue button
    fill(0, 0, 255)
    rect(10, 50, 30, 30)

    // make the "pencil" button
    fill(255)
    rect(10, 90, 30, 30)
    line(15, 105, 35, 105)

    // make the "dribbles" button
    rect(10, 130, 30, 30)
    circle(22, 145, 20)
    circle(32, 145, 10)

    // make a clear button
    strokeWeight(1)
    fill(255)
    rect(10, 210, 30, 30)
    fill(0)
    text("C", 20, 230)

    // make a save button
    fill(255)
    rect(10, 250, 30, 30)
    fill(0)
    text("S", 20, 270)

}

function mouseClicked() {

    print(int(mouseX), int(mouseY))

    // check if the mouse click was within the "red" button
    if (mouseX > 10 && mouseX < 40 && mouseY > 10 && mouseY < 40) {
        print("Clicked red button")
        brush_color = color(255, 0, 0)
    }

    // check if the mouse click was within the "blue" button
    if (mouseX > 10 && mouseX < 40 && mouseY > 50 && mouseY < 90) {
        print("Clicked blue button")
        brush_color = color(0, 0, 255)
    }

    // check if mouse clicked in "pencil" box
    if (mouseX > 10 && mouseX < 40 && mouseY > 90 && mouseY < 130) {
        print("Clicked pencil button")
        brush = "pencil"
    }

    // check if mouse clicked in the "crazytown" box
    if (mouseX > 10 && mouseX < 40 && mouseY > 130 && mouseY < 160) {
        print("Clicked dribbles button")
        brush = "dribbles"
    }

    // check if mouse clicked in "clear" box
    if (mouseX > 10 && mouseX < 40 && mouseY > 210 && mouseY < 240) {
        background(200) // clear everything
    }

    // check if mouse clicked in "save" box
    if (mouseX > 10 && mouseX < 40 && mouseY > 250 && mouseY < 280) {
        save()  // saves an image of the canvas
    }

}

```

![](interface_example.png)

#### Examples of brushes using [`random()`](https://p5js.org/reference/#/p5/random)

```js
stroke(0, 0, 0, 80)
line(mouseX, mouseY, mouseX + random(-50, 50), mouseY + random(-50, 50))
```
![](brush_1.png)

```js
noStroke()
fill(random(255), random(255), 0, 100)
circle(mouseX + random(-20, 20), mouseY + random(-20, 20), random(2, 30))
```
![](brush_2.png)

```js
line(mouseX - 20, mouseY - 20, mouseX + 20, mouseY + 20)
```
![](brush_3.png)

```js
rectMode(CORNERS) // https://p5js.org/reference/#/p5/rectMode
rect(mouseX, mouseY, pmouseX, pmouseY)
```
![](brush_4.png)

```js
stroke(0, 0, 50, 50)
line(0, 0, mouseX, mouseY)
line(width, 0, mouseX, mouseY)
line(0, height, mouseX, mouseY)
line(width, height, mouseX, mouseY)
```
![](brush_5.png)
