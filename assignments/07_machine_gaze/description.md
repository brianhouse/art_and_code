# Sketch #7: Machine Gaze

Thanks to the ubiquity of cameras, not only do you look at a digital artwork—often the artwork is looking back at you. Webcams can be a source of input to a sketch, similar to the keyboard and mouse. But video is also a rich source of information, and it captures aspects of the world that are more than just commands to the computer. Webcams are often used to bring the human body into code, for example, which raises all sorts of questions about how a machine is made to see.

For this sketch, you will make a "magic mirror" that augments or replaces a digital “reflection” of the viewer's face with additional information or graphics. Do do this, you will use a library called _clmtracker_ which gathers data about the face and provides it to your p5 code as an array of feature objects. Incorporate the coordinates in these objects into your own animations and graphics. Conceptually, your mirror should in some way address the relationship between our physical selves and how we are represented online.

Requirements:
- Your piece should be presented on a webpage
- This page should be hosted on GitHub—post a working URL to the crit Google Doc before class
- You must include your title and a [3-sentence description](../../resources/description_guidelines.md) that explains your inspiration


## Technical Resources

This assignment builds on tools we've developed so far. Please refer to the textbook and to https://p5js.org/reference/ to refresh your memory.


## Preparation

Make a folder called `mirror` and add an `index.html` file that contains the following HTML:
```html
<html>
  <head>
    <title>Machine Gaze</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.0.0/p5.js"></script>
    <script src="clmtrackr.js"></script>
    <script src="sketch.js"></script>
    <style type="text/css">
        html, body { margin: 0; padding; 0; background-color: 0}
        #p5 { position: relative; width: 800px; height: 600px; margin: auto; }
    </style>
  </head>
  <body>
      <div id="p5"></div>
  </body>
</html>

```

Download the [`clmtrackr.js`](clmtrackr.js) library and add it to your folder. This is a collection of functions written for us that will analyze the video and give us some useful objects to work with.

Finally, here is the template for `sketch.js`:

```js
let capture
let tracker

function setup() {

    createCanvas(800, 600).parent('p5')

    // start capturing video
    capture = createCapture(VIDEO)
    capture.size(800, 600)
    capture.hide()

    // create the tracker
    tracker = new clm.tracker()
    tracker.init()
    tracker.start(capture.elt)

}

function draw() {

    // draw background stuff
    background(0)

    // show the mirrored video feed
    showFlippedCapture()

    // get new data from tracker
    let features = tracker.getCurrentPosition()

    // sometimes the tracker doesn't capture anything
    // in that case, we want to stop the function right here using 'return'
    if (features.length == 0) {
        return
    }

    // 'features' is an array of objects with x, y properties
    for (let feature of features) {
        stroke(255)
        fill(255)
        circle(feature.x, feature.y, 4)
        text(feature.label, feature.x, feature.y)
    }

    // the nose is feature 62
    let nose = features[62]
    fill(255, 0, 0)
    circle(nose.x, nose.y, 30)

    // the eyes are elements 32 and 27
    fill(0, 0, 255)
    circle(features[32].x, features[32].y, 20)  // access the array directly
    circle(features[27].x, features[27].y, 20)

}

// this function flips the webcam and displays it
function showFlippedCapture() {
    push()
    translate(capture.width, 0)
    scale(-1, 1)
    image(capture, 0, 0, capture.width, capture.height)
    pop()
}
```

![](screenshot.png)


## Example Code

### Using shapes to draw features

```js
// make a new array of all the points in the left eye
let left_eye = [    features[28],
                    features[70],
                    features[31],
                    features[69],
                    features[30],
                    features[68],
                    features[29],
                    features[67]
                ]

// use a loop to make a shape vertex from each of those points
noStroke()
fill(0, 0, 255)
beginShape()
for (let eye_point of left_eye) {
    curveVertex(eye_point.x, eye_point.y)
}
endShape(CLOSE)

// draw the pupil
let left_pupil = features[32]
fill(255, 0, 0)
circle(left_pupil.x, left_pupil.y, 10)
```
![](eyeball.gif)


### Analyzing feature distances to control animation

AKA puking rainbows:
```js
let capture
let tracker
let balls = []

function setup() {

    createCanvas(800, 600).parent('p5')

    // start capturing video
    capture = createCapture(VIDEO)
    capture.size(800, 600)
    capture.hide()

    // create the tracker
    tracker = new clm.tracker()
    tracker.init()
    tracker.start(capture.elt)

}

function draw() {

    // draw background stuff
    background(0)

    // show the mirrored video feed
    showFlippedCapture()

    // get new data from tracker
    let features = tracker.getCurrentPosition()

    // sometimes the tracker doesn't capture anything
    // in that case, we want to stop the function right here using 'return'
    if (features.length == 0) {
        return
    }

//    'features' is an array of objects with x, y properties
    // for (let feature of features) {
    //     stroke(255)
    //     fill(255)
    //     circle(feature.x, feature.y, 4)
    //     text(feature.label, feature.x, feature.y)
    // }

    let mouth_top = features[60]
    let mouth_bottom = features[57]
    let distance = dist(mouth_top.x, mouth_top.y, mouth_bottom.x, mouth_bottom.y)

    let nose_tip = features[62]
    let nose_left = features[39]
    let nose_right = features[35]

    let left_nose_distance = dist(nose_tip.x, nose_tip.y, nose_left.x, nose_left.y)
    let right_nose_distance = dist(nose_tip.x, nose_tip.y, nose_right.x, nose_right.y)
    let nose_pointing = left_nose_distance - right_nose_distance
    // print(nose_pointing)


    if (distance > 10) {

        let mouth_center = { x: mouth_top.x,
                             y: (mouth_top.y + mouth_bottom.y) / 2
                         }


        let random_ball = { x: random(mouth_center.x - 20, mouth_center.x + 20),
                            y: random(mouth_center.y - 5, mouth_center.y + 5),
                            vx: random(nose_pointing / 8, nose_pointing / 4),
                            vy: random(-10, 10),
                            c: [random(255), random(255), random(255), random(200, 255)]
                        }
        balls.push(random_ball)

    }

    for (let ball of balls) {

        noStroke()
        fill(ball.c)
        circle(ball.x, ball.y, 40)

        ball.x += ball.vx
        ball.y += ball.vy

        ball.vy += 0.8

        if (ball.x < 0 || ball.x > width || ball.y < 0 || ball.y > height) {
            balls.splice(balls.indexOf(ball), 1)
        }

    }


}

// this function flips the webcam and displays it
function showFlippedCapture() {
    push()
    translate(capture.width, 0)
    scale(-1, 1)
    image(capture, 0, 0, capture.width, capture.height)
    pop()
}
```
![](rainbow_barf_cropped.gif)


### Using a mouse press to change the animation

```js
let capture
let tracker
let stars = []  // make star array

function setup() {

    createCanvas(800, 600).parent('p5')

    // set up video and tracker
    capture = createCapture(VIDEO)
    capture.size(800, 600)
    capture.hide()
    tracker = new clm.tracker()
    tracker.init()
    tracker.start(capture.elt)

    // make 200 stars
    for (let i=0; i<200; i++) {
        let new_star = {    x: random(width),
                            y: random(height),
                            vx: random(-2, 2),
                            vy: random(-2, 2),
                            radius: random(10),
                            radius_v: 1,
                        }
        stars.push(new_star)
    }

}

function draw() {

    background(0)

    let features = tracker.getCurrentPosition()
    // only take the features from index 23 on
    // doing this because I don't want the face perimeter or eyebrows
    features = features.slice(23)

    // loop through stars
    for (let star of stars) {

        // draw the star
        noStroke()
        fill(255)
        drawStar(star.x, star.y, star.radius, 3, 5)

        // do this if the mouse is pressed
        // and only do it if there are features to work with
        if (mouseIsPressed && features.length) {

            // find the index of this star in the stars array
            let index = stars.indexOf(star)

            // find a corresponding index in the features array
            // we have to do some math since there are more stars than features
            // divide the index by the length of the stars array
            // then multiply it by the length of the feature array
            // 'floor' gits rid of the fractions
            index = floor((index / stars.length) * features.length)

            // get the feature
            let feature = features[index]

            // move the star a fraction of the distance toward the feature
            star.x += (feature.x - star.x) / 10
            star.y += (feature.y - star.y) / 10

            // give it a little wiggle
            star.x += random(-1, 1)
            star.y += random(-1, 1)

        } else {

            // move the star normally
            star.x += star.vx
            star.y += star.vy

        }

        // wrap walls
        if (star.x < 0) {
            star.x += width
        }
        if (star.x > width) {
            star.x -= width
        }
        if (star.y < 0) {
            star.y += height
        }
        if (star.y > height) {
            star.y -= height
        }

        // twinkle
        star.radius -= star.radius_v
        if (star.radius < 0 || star.radius > 10) {
            star.radius_v = -star.radius_v
        }

    }

}

// adapted from https://p5js.org/examples/form-star.html
function drawStar(x, y, radius1, radius2, npoints) {
  let angle = TWO_PI / npoints;
  let halfAngle = angle / 2.0;
  beginShape();
  for (let a = 0; a < TWO_PI; a += angle) {
    let sx = x + cos(a) * radius2;
    let sy = y + sin(a) * radius2;
    vertex(sx, sy);
    sx = x + cos(a + halfAngle) * radius1;
    sy = y + sin(a + halfAngle) * radius1;
    vertex(sx, sy);
  }
  endShape(CLOSE);
}
```
![](star_man.gif)


<!--
conceptual references
zach blas
trevor paglen
kyle mcdonald
-->
