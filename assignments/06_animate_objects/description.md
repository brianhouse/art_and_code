# Sketch #5: Animate Objects

Computers are not only capable of responding to human input. Rather, within their virtual worlds, autonomous entities can follow their own sets of logic. Physics simulations, models of biological life, and abstract animations all work by defining a set of rules and seeing how things unfold with time. This is a key way in which digital media artists use code to explore processes and find unexpected aesthetic forms.

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
- [`width`](https://p5js.org/reference/#/p5/width)
- [`height`](https://p5js.org/reference/#/p5/height)
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
// variables at the top of the sketch
let x = 100
let y = 150
let size = 50
// ...
// code in the draw() function
square(x, y, size)
```
Imagine that `x`, `y`, and `size` are all variables that we're using to dynamically change the location and dimensions of this box. But what if there are _two_ boxes? Now we need something like:
```js
// variables at the top of the sketch
let box1_x = 100
let box1_y = 150
let box1_size = 50
let box2_x = 75
let box2_y = 75
let box2_size = 25
// ...
// code in the draw() function
square(box1_x, box1_y, box1_size)
square(box2_x, box2_y, box2_size)
```
This starts to get messy, and 10 boxes are going to be a problem. Enter object syntax. The above code can be replaced with this:
```js
// variables at the top of the sketch
let box_1 = {x: 100, y: 150, size: 50}
let box_2 = {x: 75, y: 75, size: 25}
// ...
// code in the draw() function
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
// variables at the top of the sketch
let box_1 = {x: 100, y: 150, size: 50}
let box_2 = {x: 75, y: 75, size: 25}
let box_3 = {x: 50, y: 20, size: 40}
//...
// code in the draw() function
square(box_1.x, box_1.y, box_1.size)
square(box_2.x, box_2.y, box_2.size)
square(box_3.x, box_3.y, box_3.size)
square(box_4.x, box_4.y, box_4.size)
```
However, using our `boxes` array and a loop, we can do it like this instead:
```js
// variables at the top of the sketch
let box_1 = {x: 100, y: 150, size: 50}
let box_2 = {x: 75, y: 75, size: 25}
let box_3 = {x: 50, y: 20, size: 40}
let boxes = [box_1, box_2, box_3]
//...
// code in the draw() function
for (let box of boxes) {
    square(box.x, box.y, box.size)
}
```
This is much more compact. `box` is a temporary variable that stands in for each of the elements in the `boxes` array in turn. The first time, `box` is `box_1`; the second time, `box` is `box_2`; and so forth for every object in the array. the This code will therefore be run 4 times, each time on a different object. 

Ok, so now we've got a new use for `{}`, plus `[]`! Watch those pairs.


### Creating objects dynamically

If we want precise objects, we've seen how to define objects in order to do it. But what if we want 100 different boxes, all with different parameters? Even with object syntax, this is still a pain.

It turns out that `random` can help us out here.

Consider the following:
```js
let random_box = {x: random(0, width), y: random(0, height), size: random(10, 100)}
```
This code creates an object with the parameters for a box in a random position and at a random size. Note that p5 doesn't let use use `random` outside of a function. But if we declare an empty array for our boxes ahead of time, we can add to it in `setup()`. Like this:
```js
let boxes = []  // declare an empty array

function setup() {

    createCanvas(windowWidth, windowHeight).parent('p5')

    // create some box parameters
    let random_box = {x: random(0, width), y: random(0, height), size: random(10, 100)}

    // add them to the array
    boxes.push(random_box)

}

function draw() {

    // draw the random box
    for (let box of boxes) {
        square(box.x, box.y, box.size)
    }

}
```

In this case, the array `boxes` has only one object in it, and only one square is drawn. But with a loop, we can create as many as we need.

Since our array is empty when we start out, we're going to use a different kind of loop than what we used above. Remember the `repeat` function from the turtle?
```js
repeat(10) {

}
```
p5 doesn't understand `repeat`, but this is the same thing:
```js
for (let i=0; i<10; i++) {

}
```
This syntax is a little awkward, but for now, just copy this and replace the 10 with however many times you want it to repeat.

Now we can add 10 b boxes to our array:

```js
let boxes = []  // declare an empty array

function setup() {

    createCanvas(windowWidth, windowHeight).parent('p5')

    // do this 10 times
    for (let i=0; i<10; i++) {

        // create some box parameters
        let random_box = {x: random(0, width), y: random(0, height), size: random(10, 100)}

        // add them to the array
        boxes.push(random_box)

    }

}

function draw() {

    // the array now has 10 elements!
    // draw all of them
    for (let box of boxes) {
        square(box.x, box.y, box.size)
    }

}
```

Our code remains very compact, but there are now 10 random boxes drawn to the screen.

This is even more helpful when we start to work with animation.


## Example Code

Colliding balls
```js
// declare our array here
let balls = []

function setup() {

    // create a canvas that fills the browser window and attach it to your HTML
    createCanvas(windowWidth, windowHeight).parent('p5')
    // the p5 variables "width" and "height" hold the dimensions of the canvas

    // loop 10 times
    // each time, create a random ball object
    for (let i=0; i<10; i++) {
        let random_ball = {     x: random(100, width-100),
                                y: random(100, height-100),
                                vx: random(5, 20),
                                vy: random(5, 20),
                                size: random(10, 100),
                                color: [random(255), random(255), random(255)],
                            }
        balls.push(random_ball)
    }

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

        // bounce ball off walls
        if (ball.x >= width - ball.size/2) {
            ball.vx *= -1
        }
        if (ball.x <= 0 + ball.size/2) {
            ball.vx *= -1
        }
        if (ball.y >= height - ball.size/2) {
            ball.vy *= -1
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

For a modification of this example that includes simulated gravity, look at the code [here](gravity.js).


<!-- flying toasters
game of life
lia
casey
turtles and traffic jams -->
