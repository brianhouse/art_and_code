# Sketch #4: Coordinate Landscape

For a painter, placing a mark on a canvas is a physical gesture—you simply touch the surface where you want the mark to be. With digital media, however, the concept of "space" is represented through symbolic coordinate systems. For example, a 2-dimensional canvas is typically understood with two numbers—an X-coordinate and a Y-coordinate—that correspond to _pixels_ (**pi** cture-**el** ements) on the screen. "Color space" can also be represented with coordinates, one each for the red, green, and blue components.

In this sketch, you will become familiar with drawing using coordinates. To explore the relationship of digital "space" to traditional depictions of the world, you will choose a [famous landscape painting from art history](https://www.google.com/search?q=famous+landscape+painting) and reinterpret it in code. This will require abstracting the original brushstrokes into geometric shapes while retaining a recognizable sense of the original composition. Pay particular attention to your use of color. The choices you make in your digital re-interpretation should communicate something distinct from the original painting.

Requirements:
- Your piece should be presented on a webpage next to an image of the original artwork
- You must include your title and [3-sentence description](../../resources/description_guidelines.md) on your webpage
- This page should be hosted on GitHub—email a working URL to the professor before class


## Technical Resources

#### Textbook

Please read Chapter 3: "Draw" (page 17) of _Getting Started with p5.js_ for this assignment, which explains in detail the p5 drawing functions.

#### p5js.org

All p5 functions are documented at https://p5js.org/reference/  

Pay particular attention to the "2D Primitives" section for this assignment


#### Shiffman

Daniel Shiffman is an educator who has produced an awesome and extensive series of videos about programming with p5. Watch these for help with this assignment:

Shapes and Drawing:  
https://www.youtube.com/watch?v=c3TeLi6Ns1E

Color:  
https://www.youtube.com/watch?v=riiJTF5-N7c


#### Colors

[Google Color Picker](https://www.google.com/search?q=color+picker)


## Technical Preparation

From now on, we will be using [p5](https://p5js.org) for our sketches. p5 sketches are also webpages—you will create a folder on your computer that contains an `index.html` file, just like you did for your homepage.

Make a folder called `landscape` and add an `index.html` file that contains the following HTML:
```html
<html>
  <head>
    <title>Coordinate Landscape</title>
    <!-- load p5 drawing functions -->
    <script src="https://cdn.jsdelivr.net/npm/p5@0.10.2/lib/p5.js"></script>
    <!-- load a local js program -->
    <script src="sketch.js"></script>
  </head>
  <body>
      <h1>Coordinate Landscape</h1>

      <!-- an empty container called p5 -->
      <div id="p5"></div>

      <!-- add other HTML in the body if you'd like -->

  </body>
</html>
```

Notice the two `<script>` tags in the head section. These tags load in javascript files like we used for Nonlinear Narrative. `p5.js` is a set of functions created for us to help us draw, and `sketch.js` is a file that you will write. Create `sketch.js` now, and save it to the same folder. This file should contain the following javascript code:

```js
// put in setup whatever needs to be done to get things started
function setup() {

    // create a 640x480 pixel canvas and attach it to your HTML
    createCanvas(640, 480).parent('p5')
    noLoop()

}

// put in draw everything you want to draw to the canvas
function draw() {

    // start off with a background
    background(200)

    // draw here!

}

// this function will print coordinates to the console whenever you click
function mouseClicked() {                
    print(int(mouseX), int(mouseY))
}
```

When you open `index.html` in your web browser, you should see a grey rectangle showing the area of the canvas.

To put your sketch online using GitHub, you will follow the [same instructions](../03_personal_homepage/description.md) as you did for your homepage. However, this time your new repository should be called "coordinate_landscape"—your URL will subsequently be http://username.github.io/coordinate_landscape


## Example Code

Coordinates in p5 are organized in a way that may be different than you are used to:
![](grid.svg)

### A basic drawing example
```js

function draw() {

    background(255)

    noStroke()              
    fill(0, 0, 255)         // R G B values from 0-255 (google search: color picker)

    rect(0, 0, 500, 100)    // x, y, width, height
    rect(0, 200, 500, 300)

    fill(255, 0, 0)
    arc(200, 150, 200, 200, 25 * PI/180, 335 * PI/180) // center x, center y, radius width, radius height, start angle, stop angle


    fill(255, 200, 0)
    ellipse(200, 150, 100, 100)   // center x, center y, radius width, radius height


    line(10, 150, 390, 150)  // x1, y1, x2, y2 (draws a line through center)


    noFill()
    stroke(0, 0, 0)          
    strokeWeight(5)         // thickness in pixels    
    rect(0, 0, 500, 300)

}
```

![](CO.png)


### Shapes, curves, and translation
```js
function draw() {

    background(255)

    strokeWeight(2)

    beginShape()
    vertex(47, 27)
    vertex(61, 181)
    vertex(165, 155)
    vertex(84, 101)
    vertex(141, 66)
    endShape(CLOSE)

    push()
    translate(150, 0)
    beginShape()
    curveVertex(47, 27)
    curveVertex(61, 181)
    curveVertex(165, 155)
    curveVertex(84, 101)
    curveVertex(141, 66)
    curveVertex(47, 27)
    endShape(CLOSE)
    pop()

    noFill()
    rect(0, 0, width, height)

}
```

![](B.png)


### HTML and p5 together

For this assignment, you will want to modify your HTML to include an artist description and the original image. You may use this template:

```html
<html>
  <head>
    <title>Coordinate Landscape</title>
    <script src="https://cdn.jsdelivr.net/npm/p5@0.10.2/lib/p5.js"></script>
    <script src="sketch.js"></script>
  </head>
  <body>
      <h1>Not so starry night</h1>

      <p>In this interpretation of Van Gogh's classic, I completely ignore everything, except the brilliance.</p>

      <img src="starry.jpg" height="400" style="float: left; margin-right: 20px;"/>

      <div id="p5"></div>

  </body>
</html>
```
