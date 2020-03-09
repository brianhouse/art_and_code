# Sketch #5: Animate Objects

Computers are not only capable of responding to human input. Rather, within their virtual worlds, autonomous entities can follow their own sets of logic. Physics simulations, models of biological life, and abstract animations all work by defining a set of rules and seeing how things unfold with time. This is a key way in which digital media artists use code to find aesthetic forms that would be otherwise unimaginable.

For this sketch, you will create an animation. You will draw from your knowledge of coordinates, colors, conditionals, and variables from the past two sketches. You will also use object syntax to keep track of what is happening on the canvas and define rules for how those objects change over time. Conceptually, your sketch should be inspired—however abstractly—by some process that happens in the real world. Examples include: snowflakes falling outside, crowds moving in a shopping mall or at a protest, players at a soccer match, termites building a nest, or mountains eroding into the sea.

Requirements:
- Your piece should be presented on a webpage
- On your webpage, you must include your title and a [3-sentence description](../../resources/description_guidelines.md) that explains your inspiration
- This page should be hosted on GitHub—email a working URL to the professor before class


### Technical Resources

#### Textbook

Please read read Chapter 8: "Motion" (page 121) of _Getting Started with p5.js_ for this assignment, which explains the concept behind animation.

Note that the chapter on motion does not work with objects. Chapter 10: "Objects" does, but it does so in a different way than we will be learning in class.


#### Shiffman

Shiffman gives a great explanation of javascript objects:  
https://www.youtube.com/watch?v=-e5h4IGKZRY

...and arrays:  
https://www.youtube.com/watch?v=VIQoUghHSxU


Useful new functions:
- [`dist()`](https://p5js.org/reference/#/p5/dist)


## Preparation

Make a folder called `animation` and add an `index.html` file that contains the following HTML:
```html
<html>
  <head>
    <title>Animate Objects</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.0.0/p5.js"></script>
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

...and this javascript code, which will make the canvas fill the browser window:

```js
function setup() {

    // create a canvas that fills the browser window and attach it to your HTML
    createCanvas(windowWidth, windowHeight).parent('p5')
    // the p5 variables "width" and "height" hold the dimensions of the canvas


}

function draw() {

    background(255, 255, 200)


}

// if the window is resized, resize the canvas to match
function windowResized() {
    resizeCanvas(windowWidth, windowHeight)
}
```

## Coding Concepts

Look out, here comes some new syntax. It will enable you to organize your code into moving parts, which will enable you to be much more expressive.


### Objects

At it's most basic level, an object is simply a collection of variables. Consider the following, in which we use the `square` function to draw a simple box:
```js
let x = 100
let y = 150
let size = 50
// ...
square(x, y, size)
```
Imagine that `x`, `y`, and `size` are all variables that we're using to dynamically change the location and dimensions of this box. But what if there are _two_ boxes? Now we need something like:
```js
let box1_x = 100
let box1_y = 150
let box1_size = 50
let box2_x = 75
let box2_y = 75
let box2_size = 25
// ...
square(box1_x, box1_y, box1_size)
square(box2_x, box2_y, box2_size)
```
This starts to get messy, and 10 boxes are going to be a problem. Enter object syntax. The above code can be replaced with this:
```js
let box_1 = {x: 100, y: 150, size: 50}
let box_2 = {x: 75, y: 75, size: 25}
// ...
square(box_1.x, box_1.y, box_1.size)
square(box_2.x, box_2.y, box_2.size)
```
Now we have compacted each set of variables into a _object_ that has a name and which has _properties_. This makes things much easier to keep track of. (Although once again we have to keep track of our `{}`s, and this time there's `:`s inside of them!)

To access the properties of an object, we use a `.` between the name of the object and the property we want to access. So the `x` property of `box_1` is simply `box_1.x`

This is really much nicer once you get the hang of it. But there's more.

### Arrays

Arrays are lists of things: numbers, strings, variables, it doesn't matter. For us, they come in particularly handy to make collections of objects.

Building off of the example above, let's make an array of objects, `boxes`, using square brackets `[]`.
```js
// these are objects
let box_1 = {x: 100, y: 150, size: 50}
let box_2 = {x: 75, y: 75, size: 25}
let box_3 = {x: 50, y: 20, size: 40}

// this is an array of objects
let boxes = [box_1, box_2, box_3]
```

Once we have this array, we can do useful things like find out how many things are in the array.
```js
boxes.length  // == 3
```
We can add things to the array, like if we had another object, `square_4`:
```js
boxes.push(box_4)
boxes.length  // == 4
```

### Loops

What arrays are really good for is for _looping_.

For example, without arrays, if we wanted to draw all of our box objects, we'd do it like this:

```js
let box_1 = {x: 100, y: 150, size: 50}
let box_2 = {x: 75, y: 75, size: 25}
let box_3 = {x: 50, y: 20, size: 40}
//...
square(box_1.x, box_1.y, box_1.size)
square(box_2.x, box_2.y, box_2.size)
square(box_3.x, box_3.y, box_3.size)
square(box_4.x, box_4.y, box_4.size)
```
However, using our `boxes` array and a loop, we can do it like this instead:
```js
let box_1 = {x: 100, y: 150, size: 50}
let box_2 = {x: 75, y: 75, size: 25}
let box_3 = {x: 50, y: 20, size: 40}
let boxes = [box_1, box_2, box_3]
//...
for (let box of boxes) {
    square(box.x, box.y, box.size)
}
```
This is much more compact. `box` is a temporary variable that stands in for each of the elements in the `boxes` array. This code will therefore be run 4 times, each time on a different object.

Ok, so now we've got a new use for `{}`, plus `[]`! Keep them straight, because as it turns out we can compact this code even further.

We don't actually need to bother to name each of these boxes. We can put the object definitions directly in the array. This code is functionally the same as the above:

```js
let boxes = [   {x: 100, y: 150, size: 50},
                {x: 75, y: 75, size: 25},
                {x: 50, y: 20, size: 40},
            ]
// ...
for (let box of boxes) {
    square(box.x, box.y, box.size)
}
```

Why would we do all of this reduction? Well, now you could fill that array with elements that you can draw and manipulate on the screen, without typing everything out individually by hand. This is particularly helpful for animation.


## Example Code

Colliding balls
```js
// declare our array here
let balls

function setup() {

    // create a canvas that fills the browser window and attach it to your HTML
    createCanvas(windowWidth, windowHeight).parent('p5')
    // the p5 variables "width" and "height" hold the dimensions of the canvas

    // we have to do this here in order to use the random function
    balls = [   {   x: random(100, width-100),
                    y: random(100, height-100),
                    vx: random(5, 20),
                    vy: random(5, 20),
                    size: random(20, 100),
                    color: [random(255), random(100), random(100)],
                },
                {   x: random(100, width-100),
                    y: random(100, height-100),
                    vx: random(5, 20),
                    vy: random(5, 20),
                    size: random(20, 100),
                    color: [random(100), random(100), random(255)],
                },
                {   x: random(100, width-100),
                    y: random(100, height-100),
                    vx: random(5, 20),
                    vy: random(5, 20),
                    size: random(20, 100),
                    color: [random(100), random(255), random(100)],
                }
            ]

}

function draw() {

    background(255, 255, 200)

    for (let ball of balls) {

        // move the objects
        ball.x += ball.vx
        ball.y += ball.vy

        // draw the objects at the new location
        noStroke()
        fill(ball.color)
        circle(ball.x, ball.y, ball.size)

        // now update vx and vy for next time

        // add some gravity
        ball.vy += 0.2          // gravity!

        // bounce ball off walls
        if (ball.x >= width - ball.size/2) {
            ball.vx *= -1
        }
        if (ball.x <= 0 + ball.size/2) {
            ball.vx *= -1
        }
        if (ball.y >= height - ball.size/2) {
            ball.vy *= -.8 // dampen the floor somewhat
        }
        if (ball.y <= 0 + ball.size/2) {
            ball.vy *= -1
        }

        // check if it is colliding with another balls
        // let collisions = 0
        for (let other_ball of balls) {
            if (other_ball != ball) {   // don't compare with itself!

                // how close do they have to be to touch?
                let touching = abs(ball.size/2 + other_ball.size/2)

                // how far apart are they now?
                let distance = dist(ball.x, ball.y, other_ball.x, other_ball.y)

                // if theyre touching, bounce them
                // (not real physics, but close enough for now)
                if (distance <= touching) {
                    ball.vx *= -1
                    ball.vy *= -1
                    ball.x += ball.vx
                    ball.y += ball.vy
                }

            }
        }

    }

}

// if the window is resized, resize the canvas to match
function windowResized() {
    resizeCanvas(windowWidth, windowHeight)
}
```


<!-- flying toasters
game of life
lia
casey
turtles and traffic jams -->
