# Time

So far, all of the code we've written runs all at once and produces a static output. However, computers are quite good at incorporating another dimension: time.


### Event Handlers

To work with time, we have to set up our sketches a bit differently, using what's called **event handlers**. These are a special type of function. We've already used plenty of built-in functions to make the various shapes on the canvas. However, event handlers are functions we'll write ourselves.

Because event handlers have specific names, Processing will know to call those functions for us under certain circumstances.

The first is `setup()`, which is also the most boring. This function is called once when the sketch is first run:

<p align="center">
  <img src="code/canvas_1__.png" width=600 /><br />
</p>

Notice how this function runs even though we didn't call it explicitly.

Once we start using handlers, _all_ of our code has to be contained in functions. So `setup()` doesn't do much for us other than give us a place to put the kind of code we've been working with so far—that is, code that is intended to be run just once. For example, from now on, we'll put `size()` inside of setup.

The interesting stuff starts with `draw()`. Processing calls `draw()` over and over again, once every 1/60th of a second. The implications of this are profound, because it allows us to do animation (the reason that it is 1/60th of a second is that this is the standard frame rate for digital video).

To start with, let's draw a circle:

```py
def setup(): # runs just once
    size(400, 400)

def draw(): # runs over and over again
    circle(width/2, height/2, 30)    
```

<p align="center">
  <img src="code/canvas_2.png" width=400 /><br />
</p>

So far, `setup()` is called right when the sketch is run, and it initializes the canvas. Then, `draw()` is called and it in turn calls `circle()`. In fact, the code inside `draw()` is running 30 times every second, drawing circle upon circle upon circle. However, we can't see this, because it's always drawing the circle at the same position.

Note the indentation—the `def` of the draw function is all the way over to the left, it's not underneath `setup()`.

To change the position of the circle, we're going to need some more functions. 


### Simple Motion


Before we go further, let's add some functions to our sketch. These functions aren't built-in, like `circle`, and we're not going to write them from scratch. Rather, we're just going to paste in some pre-written code to add some functionality. We won't go over exactly how they work now, but most of what's in them will be covered as we go on.

Put them at the bottom, like this:

```py
def setup(): # runs just once
    size(400, 400)

def draw(): # runs over and over again
    circle(width/2, height/2, 30)    
    
        
                
def change(start, stop, duration, offset=0):
    return map((frameCount + offset) % max(duration, 1), 0, duration, start, stop)

def swing(start, stop, duration, offset=0): 
    position = -cos(2 * PI * change(0, 1, duration * 2, offset)) * .5 + .5
    return (position * (stop - start)) + start  
```

Going forward in this document, I won't show these two functions to avoid the clutter with every example. Just remember that they're down there!

Now, let's make the circle move. Replace the `width/2` that we're using as an argument for the circle's x position with `change(0, width, 120)`. Just like with `random()`, we're putting a function where a single argument was before.


```py
def setup(): # runs just once
    size(400, 400)

def draw(): # runs over and over again
    circle(change(0, width, 120), height/2, 30)    
```

`change()` takes three arguments: start value, stop value, and duration in terms of the number of frames. Remember, Processing is calling `draw()` 60 times a second, so putting 120 for the duration means that `change()` will start at its start value and transition to its stop value over the course of two seconds. Here's the result:

<p align="center">
  <img src="code/canvas_3.gif" width=400 /><br />
</p>

The circle moves! Or rather, the circle is being redrawn at a new location every frame. The trail of circles looks pretty cool, but to make this really feel like animation, we have to clear our canvas every frame, using `background()`:

```py
def setup(): # runs just once 
    size(400, 400)

def draw(): # runs over and over again
    background(255) # clear the background every frame    
    circle(change(0, width, 120), height/2, 30)    
```

<p align="center">
  <img src="code/canvas_4.gif" width=400 /><br />
</p>


`swing()` works the same as `change()` — it just switches direction and goes back again.

```py
def setup():
    size(400, 400)

def draw():
    background(255)
    circle(swing(0, width, 120), height/2, 30)   # swing
```        

<p align="center">
  <img src="code/canvas_5.gif" width=400 /><br />
</p>

What happens if you do both at the same time?

<p align="center">
  <img src="code/canvas_6.gif" width=400 /><br />
</p>

```py
def setup(): # runs just once 
    size(400, 400)

def draw():
    background(255)
    circle(swing(100, width-100, 120, 60), swing(100, height-100, 120, 0), 30)
    circle(swing(120, width-120, 100, 50), swing(120, height-120, 100, 0), 30)
```           

In the example above, there are two moving circles. In each one, both the x and the y position are controlled by `swing()` functions. One of which is making a circle 100 pixels from the edge, the other one is 120 pixels from the edge. 

To get this to work, we use the fourth parameter of `swing()` (and `change()`), which is "offset". Notice how in the first circle, the duration is 120 frames, and the x position function is offset by 60 frames. That puts the x and y in a complementary relation to each other, generating a circle. In the second circle, the duration is 100 frames, so the offset is 50.

Play with those offset values, and see what you get!


### Compound Motion

By adding multiple motion functions together, more complex motion results. For example, you may want to have something moving across the screen while simultaneously moving more subtly within itself. For example, a falling leaf (ok, it's not a very good leaf, but roll with it):

<p align="center">
  <img src="code/canvas_7.gif" width=400 /><br />
</p>

```py
def setup(): 
    size(400, 400)
    
def draw():
    background(255)        
    fill(0, 255, 0)
    noStroke()
    circle(width/2 + swing(-42, 42, 50), change(0, height, 500) + swing(-12, 12, 28), 22)
```

Notice how in the x parameter, `swing()` is added to `width/2`. This is another way of writing `swing(width/2 - 42, width/2 + 42, 50)`. The effect is the "leaf" oscillating left and right.

With the y parameter, `change()` and `swing()` are added together. While `change()` is making the leaf fall from the top to the bottom of the screen, `swing()` complicates this motion a bit, by making it go up and down against that general motion.

All together, it's a relatively complex motion that gives a nuanced character to the motion.


### Time Conditionals

There's another entirely different way to deal with time, and that is through conditionals. 

Conditionals are a fundamental structure in coding whereby depending on some condition, one thing happens—or another. In this case, we'll be using the Processing variable `frameCount`. This magic variable, much like `width` and `height` is automatically set by Processing. It holds the number of frames since the sketch was started. 

For example, if we want something to begin after 100 frames, we write:

```py

if frameCount >= 100:  # if 100 or more frames have elapsed
    # do the thing

```

Likewise, if we want something to stop after 100 frames, we can write:

```py

if frameCount < 100:  # if less than 100 frames have elapsed
    # do the thing

```

Or we can have two conditions together:

```py

if 100 <= frameCount < 200:  # if 100 or greater, but less than 200 frames have elapsed
    # do the thing

```

Notice how `<=` and `>=` versus `<` and `>` are used above. You want to make sure you keep track of whether you're including the boundary in your condition or not.


Imagine a sketch that shows the changing seasons. We may want four different colored backgrounds for Spring (green), Summer (yellow), Autumn (orange), and Winter (white). We can do that with four conditionals:

```py
def setup(): 
    size(400, 400)
    
def draw():
    if frameCount < 200:
        background(0, 255, 0)
    if 200 <= frameCount < 400:
        background(255, 255, 0)
    if 400 <= frameCount < 600:
        background(255, 165, 0)
    if 600 <= frameCount < 800:
        background(255)   
```

<p align="center">
  <img src="code/canvas_8.gif" width=400 /><br />
</p>


This example begs the question, however: If `frameCount` keeps going up, is it possible to make it repeat?

The answer is to use an operator called mod, `%`. You may be familiar with this from math, but what it does is calculate the remainder of a value when divided by a given number. What? In other words, it makes a value loop once it reaches a certain number. 

So in this case, let's replace `frameCount` with `frameCount % 800`. In effect, this makes `frameCount` count from 0 to 799 and then start over again—and our seasons repeat.



### Color

Motion doesn't always have to be spatial—applying it to color is another effective approach. However, at this point the limitations of R,G,B can come into play. For example, maybe you want to change the brightness of a color, but not its hue. How can we do that?

Processing actually supports another color mode, HSB, which stands for Hue, Saturation, and Brightness. To use HSB, put this in your setup function:

    colorMode(HSB, 360, 100, 100)

Now, if you use `fill()` or `stroke()` the three parameters will be HSB instead of RGB (opacity is still the fourth)

<p align="center">
  <img src="code/hsb.png" width=500 /><br />
</p>

To navigate these values, go to the menubar and choose "Tools" -> "Color Selector...". You can see that Hue is a degree value from 0–360, and Saturation and Brightness are percentages from 0–100. Play around to get a sense of how they relate.

In practice, we can use this to create smooth transitions either between colors or within a color. For example, a pulsing red background:

```py
def setup(): 
    size(400, 400)
    colorMode(HSB, 360, 100, 100)
    
def draw():
    background(0, 100, swing(0, 100, 100))
```

<p align="center">
  <img src="code/canvas_9.gif" width=400 /><br />
</p>





