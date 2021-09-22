# Indeterminacy

## Concept

The physical world is very complex—so much so that it is never fully predictable. From the shape of a leaf to the gait of an animal to the words you use to express a thought, variation is intrinsic to reality. This is intuitive to art-making in physical mediums. When a paintbrush flows against a canvas, the individual hairs move in a way that creates texture; when musicians play a score, the air responds dynamically to create rich timbres.

Digital media, however, encode everything in numbers. As we saw previously with coordinates, this can entail defining everything very precisely, rather than intuitively relying on the indeterminate properties of the medium. But to manually reproduce the degree of variation we see in nature would be tedious, if not impossible.

However, algorithms have been developed to simulate "random"—e.g. unpredictable—numbers. Such indeterminacy can be used to create variation on forms that simulates the dynamics of the physical world, or at least expands the possibilities of what can be automatically generated in digital imagery.


## Context

### Non-digital

How do we generate randomness without a computer? Consider dice, flipping coins, shuffling cards...

Algorithms for working with indeterminacy have been an important part of artmaking even without electronic computers. The [Dada](https://en.wikipedia.org/wiki/Dada) movement, for example, developed the "chance collage" technique, in which artists dropped scraps of paper onto a larger sheet and pasted them wherever they landed. This method of embracing chance was a reaction against the ideologies of power and control that had led to the outbreak of WWI in Europe in the late 1910s.

<p align="center">
  <img src="context/1_arp.jpg" width=500 /><br />
  Jean Arp, <i>According to the Laws of Chance</i> (1933)<br />
</p>

In the United States, the term "indeterminacy" is often associated with the composer and conceptual artist [John Cage](https://en.wikipedia.org/wiki/John_Cage) (1912–1992). His piece _Music of Changes_ (1951) arranged notes and rests on a score according to an elaborate system of chance that involved throwing sticks on the ground and interpreting how they landed. He appropriated this technique from the _I Ching_, an ancient Chinese text (1000–750 BCE) which intended it as a means of [divination](https://en.wikipedia.org/wiki/Divination). This is similar to using tarot cards, rolling dice, or flipping a coin, all of which are manifestations of chance in culture that have been used by artists to generate indeterminacy.

<p align="center">
  <img src="context/2_cage.png" height=500 /><br />
  John Cage, from <i>Music of Changes</i> (1951) [<a href="https://www.youtube.com/watch?v=B_8-B2rNw7s">listen here</a>]<br />
</p>

Of course, incorporating nonhuman agency is another way of relinquishing a degree of control over a finished result. Daniel Ranalli did this in a simple way with snails:

<p align="center">
  <img src="context/3_ranalli.jpg" width=500 /><br />
  Daniel Ranalli, <i>Double Line</i> (2007)<br />
</p>


### Digital

When it comes to computers, one way of generating random numbers is to measure some chaotic physical phenomena, like cosmic background radiation, and incorporating those numbers into a program. This can be done directly with sensors or via copying a previously generated series of numbers from a published reference like [_A Million Random Digits_](https://www.youtube.com/watch?v=bvLD54GnOTk), which was created by the RAND corporation for this purpose in 1955.

A more practical way that we use today is a "pseudo-random number generator," an algorithm that takes a "seed" (like the current time) and [elaborates upon it](https://en.wikipedia.org/wiki/Mersenne_Twister) in a complex way. The resulting numbers are in fact a repeating finite sequence and therefore not strictly indeterminate, but for most purposes they are plenty random. Many programming languages (including Python) include a function, usually called `random`, that lets us use these numbers.

Digital media artists have seized upon the opportunity to experiment. One example is [Harold Cohen](https://en.wikipedia.org/wiki/Harold_Cohen_(artist)) (1928–2016), who starting in the 1960s began developing an algorithm to make unique representational drawings using rules together with random arguments. His code chooses the overall composition of the images as well as approximates the indeterminate aspects of lines made with a pen. He and others have made the specious claim that his program, which he called AARON, is an example of artificial intelligence—it is not, but it nonetheless demonstrates how powerful the random function can be.

<p align="center">
  <img src="context/4_aaron.jpg" width=500 /><br />
  Harold Cohen, painting by <i>AARON</i> (1995)<br />
</p>

A contemporary of Cohen's, Roman Verostko (1929–), approached indeterminacy with a very different aesthetic, even though his work similarly uses random arguments within repeating patterns. Rather than approximate images made by hand, Verostko uses code to craft beautiful abstract forms that show an Eastern aesthetics and reflect his his mystic interests (he also spent time as a Benedictine monk). Verostko is also known for initiating the "[algorist](https://en.wikipedia.org/wiki/Algorithmic_art#Algorists)" movement of artists who work with computers.

<p align="center">
  <img src="context/5_verostko.jpg" width=500 /><br />
  Roman Verostko, <i>FlyingCloud II</i> (1999)
</p>

[Casey Reas](https://en.wikipedia.org/wiki/Casey_Reas) (1972–), together with Ben Fry, is the creator of Processing. They realized that using a common platform to generalize many of the techniques used by earlier algorithmic artists would be better than artists always having to start from scratch, and that sharing code would create a community of artists working with code. The use of `random` to produce repetition with variation features prominently in Reas' own work.

<p align="center">
  <img src="context/6_reas.jpg" width=500 /><br />
  Casey Reas, <i>Process 18 (Software 2)</i> (2010)
</p>

Another notable artist who uses Processing goes by the name [LIA](https://en.wikipedia.org/wiki/Lia_(artist)). Her work often takes the form of animation, with infinitely evolving visuals that she performs live or which are displayed on a monitor within a frame.

<p align="center">
  <img src="context/7_lia.png" width=500 /><br />
  LIA, <i>Untitled 20160817</i> (2016)
</p>

The work of contemporary artists like Reas and LIA is often called "generative art." This reflects the fact that when a code-based artwork heavily relies upon indetermine processes, each time the program is run, it will produce a difference output. Therefore, the code "generates" an infinite number of similar pieces, which shifts the emphasis away from the output and toward the code itself as the actual artwork.


## Code

A critical function for making images like these is `random()`. `random()` doesn't draw anything to the canvas itself. Instead, it produces a random number within a given range.

```py
random(0, 100)  # a random number between 0 and 100
```

If you put this into a sketch, every time you run it, you'll get a different random number. But we can't see that number unless we print it out:

```py
print(random(0, 100))
```

Notice how we've put `random()` _inside_ `print()`. It can be tricky to keep track of all the parentheses, but this is a very useful thing to be able to do. `random()` will first do its job and come up with a random number between 0 and 100, and then this number will be what `print()` prints out. And every time the sketch is run, this number will be different:

<p align="center">
  <img src="code/canvas_1_.png" width=700 /><br />
</p>

 Try seeing what happens if you change `0` and `100` to other values, for example `-20` and `20`:

 <p align="center">
   <img src="code/canvas_11.png" width=700 /><br />
 </p>

As an aside, one shortcut that will make our lives a bit easier is that if the first argument for `random` is `0`, we can omit it. In other words `random(0, 42)` can be shortened to `random(42)`, which is more convenient to write.

<!-- pause and have them experiment, questions -->

### Random arguments

Ok, so what can we do with this visually?

Let's start with a simple shape in the center of the canvas:

```py
size(500, 400)

circle(250, 200, 100) # x position, y position, diameter
```

<p align="center">
  <img src="code/canvas_2.png" width=500 /><br />
</p>

What if we used random numbers for the arguments in `circle()` instead?

If we want coordinates that fit within the canvas, we want them to be between 0 and its width or height. Since we're using 0, we can omit that argument. Therefore, `random(500)` and `random(400)` produce numbers between 0 and the width and height of the canvas, respectively.

```py
size(500, 400)

circle(random(500), random(400), 100) # x position, y position, diameter
```

This looks a little weird with all the parentheses and commas (be careful to keep track of them all!), but all we've done is _substitute_ the static numbers that we were using with the `random` function and its arguments:
- `250` is replaced with `random(500)` which chooses a number between 0 and 500
- `200` is replaced with `random(400)` which chooses a number between 0 and 400

The result is that every time you run this sketch, the circle will be drawn in a different location:


<p align="center">
  <img src="code/canvas_3.png" width=500 /><br />
</p>

<!-- questions -->

How is that at all useful? Well, what if we repeated that random circle a bunch of times using a `for` loop (and also substituted the diameter with a random argument between 10 and 300)?

```py
size(500, 400)

for i in range(10):
    circle(random(500), random(400), random(10, 300))
```

<p align="center">
  <img src="code/canvas_5.png" width=500 /><br />
</p>

Suddenly, this has become very expressive with just a little code.

It turns out that `random` can be applied to color, not just shapes. Remember than every component of a color goes from 0-255, which means we can make random numbers like this:
```py
# a random color with a random amount of opacity (R, G, B, opacity)
fill(random(255), random(255), random(255), random(255))

# a random greyscale color with a random amount of opacity (grey, opacity)
fill(random(255), random(255))
```

Let's use this together with a loop to make a somewhat more elaborate example:

```py
size(500, 400)

# no outline on the shapes
noStroke()

# repeat 100 times
for i in range(100):

    # choose random color and opacity
    fill(random(255), random(255), random(255), random(255))  

    # make a random triangle with the bounds of the canvas
    triangle(random(500), random(400), random(500), random(400), random(500), random(400))

```

<p align="center">
  <img src="code/canvas_6.png" width=500 /><br />
</p>

Now we're getting somewhere. If you play with the arguments, and add in more of the drawing tools we've learned previously, you can get an increasingly more interesting result:

```py
size(500, 400)

# set the background to white
background(255)

# repeat everything 20 times
for i in range(20):

    # make a random triangle with no outline and a random red-ish fill
    noStroke()
    fill(random(255), 0, 0, random(255)) # choose random red value and opacity (green and blue are 0)
    triangle(random(500), random(400), random(500), random(400), random(500), random(400))

    # make a circle with no fill and random greyscale outline of random weight
    noFill()
    stroke(random(255), random(255))
    strokeWeight(random(1, 10))
    circle(random(500), random(400), random(10, 50))
```

<p align="center">
  <img src="code/canvas_7.png" width=500 /><br />
</p>

As you can see, even this relatively straightforward example shares a certain aesthetic with that of artists we've seen who work with indeterminacy.

Remember that you don't always have to use the entire width and height of the canvas with random. In fact, experimenting with these ranges is how you can add structure to your sketch.

In this example, which has a canvas size of 640 x 480, notice that the blue rectangles get a random horizontal position between 0 and 320, and the red ellipses get a random horizontal position between 320 and 640:

```py
size(640, 480)
background(255)
noStroke()

for i in range(100):

    # blue rectangles
    fill(255, 0, 0, 128)
    rect(random(320), random(480), random(10, 100), random(10, 100))

    # red ellipses
    fill(0, 0, 255, 128)
    ellipse(random(320, 640), random(480), random(10, 100), random(10, 100))

```

<p align="center">
  <img src="code/canvas_12.png" width=500 /><br />
</p>

We could also cluster the circles within a smaller overall area in the center. Here, the rectangles once again take up the whole canvas, but the ellipses have more constrained arguments:

```py
size(640, 480)
background(255)
noStroke()

for i in range(100):

    # blue rectangles
    fill(255, 0, 0, 128)
    rect(random(640), random(480), random(10, 100), random(10, 100))

    # red ellipses
    fill(0, 0, 255, 128)
    ellipse(random(220, 420), random(140, 340), random(10, 100), random(10, 100))
```

<p align="center">
  <img src="code/canvas_13.png" width=500 /><br />
</p>

Notice how the rectangles and ellipses are interleaved. This is because for every iteration of our loop, the computer draws one rectangle and then one ellipse. What if we wanted all the rectangles drawn first?

To do that, we use two separate loops (and we're very careful with indentation):

```py
size(640, 480)
background(255)
noStroke()

# red rectangles    
for i in range(100):
    fill(255, 0, 0, 128)
    rect(random(640), random(480), random(10, 100), random(10, 100))

# blue ellipses
for i in range(100):
    fill(0, 0, 255, 128)
    ellipse(random(220, 420), random(140, 340), random(10, 100), random(10, 100))
```

<p align="center">
  <img src="code/canvas_14.png" width=500 /><br />
</p>

Now all the ellipses are all up front. This technique is a simple way to create a sense of composition.

### Random with nested loops

In all of these examples, we've been ignoring `i`. But we can certainly combine `random()` with the techniques we used to organize shapes via loops. This is one way to create tension between regularity and variability, such as in the work of Vera Molnár.

First consider a regular grid:
```py
size(640, 480)
background(255)

for i in range(16):
    for j in range(12):
        square((i * 40) + 5, (j * 40 ) + 5, 30)
```        
<p align="center">
  <img src="code/canvas_16.png" width=500 /><br />
</p>

To give this a sense of variation, let's change the offset by a small random amount:
```py
size(640, 480)
background(255)

for i in range(16):
    for j in range(12):
        square((i * 40) + random(2, 8), (j * 40 ) + random(2, 8), 30)
```   
<p align="center">
  <img src="code/canvas_17.png" width=500 /><br />
</p>

Here we still understand the canvas as a grid, but the tension in the variation creates a more satisfying aesthetic result.

Instead of positioning, we might randomly vary the construction of a series of small multiples, using a third nested loop. Individually, these figures might not be all that interesting, but together they create a world of curiosities:

```py
size(640, 480)
background(255)

for i in range(16):
    for j in range(12):
        for k in range(5):
            ellipse((i * 40) + 20, (j * 40) + 20, random(5, 35), random(5, 35))
```


<p align="center">
  <img src="code/canvas_15.png" width=500 /><br />
</p>

Random arguments and loops together radically transform how we can think about making images—rather than just encoding space, the computer can do some work for us by incorporating indeterminacy, work that can surprise us and add visual depth to our compositions.


### Flipping a coin

By specifying the ranges of random parameters, we can do a lot to control the texture and composition of the work. But what if we want to simply do one thing OR another? To make something blue OR red, for example, or a circle OR a square, or some other more radical branch in the code?

Consider the following construction:

```py
size(640, 480)

if random(1) > .5:      # flip the coin
    fill(255, 0, 0)     # this happens 50% of the time
else:
    fill(0, 0, 255)     # this happens 50% of the time

square(320, 240, 100)
```

This is called a random conditional, and it takes the form of an `if` statement. Notice how there are two blocks of code—one with a red fill and one with a blue fill—and only _one_ of them will actually run. Which one runs depends on whether `random()` returns a value that is above or below .5. We can read this like an English sentence: "if a random number between 0 and 1 is above .5, make it red, else make it blue."

We'll cover conditionals in detail in our next unit, but previewing it here will give us some flexibility to produce more radically different versions of the output each time we run the code.

Why would we want that? This is a strategy often used in generative art: if the same code is being used to produce multiple versions of an artwork in a series, random conditionals can contribute to those versions being more radically unique.
