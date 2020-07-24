# Final Project

In this course, we have explored scores for humans and for the computer, we've made nonlinear narratives with branching conditions, worked with coordinate systems for space and color, incorporated interface elements for interaction, created objects with their own ways of moving, and brought ourselves into code through the camera. All of these are formal components to code-based digital media; along the way we've also heard about many artists who use various aspects of these forms in their own practices.

For your final project, you may draw from any of these techniques (and/or experiment with other ones) to develop a sketch of your own design. This is your chance to move beyond the prescriptions of the assignments thus far, and to focus on what most interests you.

As always, you are required to have a title and artist description. However, for this assignment, a draft of your artist description will be due up front (4/20). We will have a preliminary crit the following week (4/27) where you will receive feedback on what you've produced so far, and then the final work will be due for the end of the semester.

For your final, in addition to this project, you will update your website to include links to all of your assignments (except Nonlinear Narrative) as a portfolio of your work in this class. This will also be a reference for you in the future to go back and remember what you've done and how you did it.


## Example Code

Additional references and techniques will be posted here as they come up in our discussion, in addition to the class Slack.

### True fullscreen

Break out of the browser, and fill the entire screen with your sketch. For browser security reasons, [this command](https://p5js.org/reference/#/p5/fullscreen) has to be run in response to a mouse click, and you'll want to adjust the canvas size dynamically.

```js
function mouseClicked() {

    fullscreen(true)

}

function windowResized() {

    resizeCanvas(windowWidth, windowHeight)

}
```


### Using external images and sounds in sketches

Because p5 runs in the browser, and because browsers have security restrictions that prevent it from accessing your files directly, there are a few extra steps if you want to load images directly in a p5 sketch. Specifically, you must run your sketch from a local web server. A "server" is simply a computer that provides access to a folder of files via HTTP—ie, the web. GitHub is already a server, so the following only applies to running your sketch locally. Once you've uploaded it, it should work as expected.

The p5 website outlines [a few ways to run a local server](https://github.com/processing/p5.js/wiki/Local-server).

The easiest is to install [Web Server for Chrome](https://chrome.google.com/webstore/detail/web-server-for-chrome/ofhbbkphhbklhfoeikjpcbhemlocgigb/).

When the extension is up and running, you'll point your browser at the URL showing on Chrome Web Server, which will look something like http://127.0.0.1:8887

(If you have installed the extension, but you can't figure out how to launch it, [visit this link](https://chrome.google.com/webstore/detail/web-server-for-chrome/ofhbbkphhbklhfoeikjpcbhemlocgigb/).)

Once that is all up and running, you'll be able to load images, sounds, and even videos into your sketches. For sound, you'll also need to have the p5.sound addon loaded. That happens in the HTML with another link to a script:

```html
<html>
  <head>
    <title>Loading Example</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.0.0/p5.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.0.0/addons/p5.sound.js"></script>
    <script src="sketch.js"></script>
    <style type="text/css">
        html, body { margin: 0; padding; 0; }
    </style>
  </head>
  <body>
      <div id="p5"></div>
  </body>
</html>
```

And here's a `sketch.js` example of how to load an image, draw it at the mouse position, and play a sound effect when the mouse is clicked:

```js
let pio
let bark

function preload() {

    pio = loadImage("pio.jpg")
    bark = loadSound("bark.mp3")

}

function setup() {

    createCanvas(windowWidth, windowHeight).parent('p5')

}

function draw() {

    background(0)

    image(pio, mouseX, mouseY, pio.width, pio.height)

}

function mouseClicked() {

    bark.play()

}
```

Note that sounds cannot play automatically as soon as the sketch loads—this is another security feature of browsers that prevents advertisements from taking over your web experience. As long as the mouse has been clicked at least once (or the keyboard pressed), the sound can play.


### Using fonts in sketches

You can use external fonts in your p5 sketches—any .ttf or .otf font file will work. Many fonts are available for free online (one good source is [1001freefonts.com](https://www.1001freefonts.com)). If you download a font, it may come in a zip file, and you may have to unzip it first to get at the actual font file. Once you do, follow the steps below to integrate it into your sketch.

In addition, Allison Parrish has a fantastic tutorial on using text and type in p5.js: [https://creative-coding.decontextualize.com/text-and-type/](https://creative-coding.decontextualize.com/text-and-type/)

```js

// Step 1:
// put a .ttf or .otf file in the same folder as sketch

// Step 2:
// declare a variable to hold your font data
let paladinFont

// Step 3:
// load the font data using the preload and loadFont functions
function preload() {

    paladinFont = loadFont("PaladinFLF.ttf")

}


function setup() {

    createCanvas(windowWidth, windowHeight).parent('p5')

}

function draw() {

    background(0)

    // Step 4:
    // use the font functions to draw the font
    fill(0, 255, 0)          // set color for the text
    textFont(paladinFont)    // set the font to your variable
    textSize(36)             // set text size
    text("Hello World", mouseX, mouseY)  // draw the text at x,y

}

// Step 5:
// Use the Web Server for Chrome extension to select your project folder, and
// visit the corresponding URL in the browser.
//
// Because fonts are an external media file, just like images and sounds, your /// browser will block it from loading if you try to open index.html directly.
```
![](hello_font.gif)


### Using video

 Video works much the same way as other external files but with a few extra commands. You’ll have to use Chrome Web Server Extension to have videos work, just like with images, sounds, and fonts.

```js
let prince_vid

function preload() {

    prince_vid = createVideo('prince_internet.mp4')
    prince_vid.hide()   // include this or you'll get a second video outside the canvase

}


function setup() {

    createCanvas(windowWidth, windowHeight).parent('p5')

}

function draw() {

    background(0)

    image(prince_vid, 100, 100, prince_vid.width, prince_vid.height)

}

function mouseClicked() {

    prince_vid.play()
    prince_vid.time(15)     // skip 15 seconds in
    // prince_vid.loop()
    // prince_vid.stop()

}
```


### Interpolating colors

These examples make use of the p5 function [`lerpColor`](https://p5js.org/reference/#/p5/lerpColor).


```js
function draw() {

    let color_1 = color(255, 0, 0)      // red is our first color
    let color_2 = color(0, 0, 255)      // blue is our second color

    // use a for-loop and line to draw each row of pixels across the screen individually
    // each time, change the lerp value
    for (let y=0; y<height; y++) {
        let lerped_color = lerpColor(color_1, color_2, y / height)
        stroke(lerped_color)
        line(0, y, width, y)
    }

}
```

![](lerpscreen.png)

```js
function draw() {

    let color_1 = color(255, 0, 0)      // red is our first color
    let color_2 = color(0, 0, 255)      // blue is our second color

    // fade_amount has to be between 0 and 1
    // by taking the mouseY value and dividing it by the height of the screen
    // we get a value between 0 and 1 which represents how far up the screen the
    // mouse is currently positioned
    let fade_amount = mouseY / height
    let lerped_color = lerpColor(color_1, color_2, fade_amount)

    //// or try using frameCount()
    // let fade_amount = frameCount / 500
    // let lerped_color = lerpColor(color_1, color_2, fade_amount)

    //// or an object variable (see object declaration above)
    // let fade_amount = changing_color.c / 500
    // let lerped_color = lerpColor(color_1, color_2, fade_amount)
    // changing_color.c += changing_color.vc
    // if (changing_color.c == 0 || changing_color.c == 500) {
    //     changing_color.vc = -changing_color.vc
    // }

    background(lerped_color)

}
```
![](lerp.gif)


### Clicking on moving objects

```js
// array for moving objects
let balls = []

function setup() {

    createCanvas(windowWidth, windowHeight).parent('p5')

    // make 5 random ball objects
    for (let i=0; i<5; i++) {
        // the x and y leav room on the edges for the ball radius
        let random_ball = { x: 50 + random(width-100),
                            y: 50 + random(height-100),
                            vx: random(-5, 5),
                            vy: random(-5, 5),
                            c: [random(255), random(255), random(255)]
                        }
        balls.push(random_ball)
    }

}

function draw() {

    background(0)

    for (let ball of balls) {

        // draw objects
        noStroke()
        fill(ball.c)
        circle(ball.x, ball.y, 100)

        // update objects
        ball.x += ball.vx
        ball.y += ball.vy

        // bounce off walls
        if (ball.x <= 50 || ball.x >= (width - 50)) {
            ball.vx = -ball.vx
        }
        if (ball.y <= 50 || ball.y >= (height - 50)) {
            ball.vy = -ball.vy
        }

    }

}


function mouseClicked() {

    for (let ball of balls) {

        // calculate the distance from the mouse to the ball
        let distance = dist(mouseX, mouseY, ball.x, ball.y)

        // if the distance is less than the ball's radius, the click is inside
        if (distance < 100) {

            // change the color
            ball.c = [random(255), random(255), random(255)]

        }

    }

}
```
![](ball_click.gif)
