# Indeterminacy

## Concept

The physical world is very complex—so much so that it is never fully predictable. From the shape of a leaf to the gait of an animal to the words you use to express a thought, variation is intrinsic to reality. This is intuitive to artmaking in physical mediums. When a paintbrush flows against a canvas, the individual hairs move in a way that creates texture; when musicians play a score, the air responds dynamically to create rich timbres.

Digital media, however, encode everything in numbers. As we saw in the last unit, this can entail defining everything very precisely, rather than intuitively relying on the indeterminate properties of the medium. But to manually reproduce the degree of variation we see in nature would be tedious, if not impossible.

However, algorithms have been developed to simulate "random"—e.g. unpredictable—numbers. Such indeterminacy can be used to create variation that simulates the dynamics of the physical world, or at least expands the possibilities of what can be automatically generated in digital representations.


## Context

### Non-digital

Algorithms for working with indeterminacy have been an important part of artmaking even without electronic computers. The [Dada](https://en.wikipedia.org/wiki/Dada) movement, for example, developed the "chance collage" technique, in which artists dropped scraps of paper onto a larger sheet and pasted them wherever they landed. This method of embracing chance was a reaction against the ideologies of power and control that had led to the outbreak of WWI in Europe in the late 1910s.

<p align="center">
  <img src="arp.jpg" width=500 /><br />
  Jean Arp, <i>According to the Laws of Chance</i> (1933)<br />
</p>

In the United States, the term "indeterminacy" is often associated with the composer and conceptual artist [John Cage](https://en.wikipedia.org/wiki/John_Cage) (1912–1992). His piece _Music of Changes_ (1951) arranged notes and rests on a score according to an elaborate system of chance that involved throwing sticks on the ground and interpreting how they landed. He appropriated this technique from the _I Ching_, an ancient Chinese text (1000–750 BCE) which intended it as a means of [divination](https://en.wikipedia.org/wiki/Divination). This is similar to using tarot cards, rolling dice, or flipping a coin, all of which are manifestations of chance in culture that have been used by artists to generate indeterminacy.

<p align="center">
  <img src="cage.gif" width=500 /><br />
  John Cage, from <i>Music of Changes</i> (1951) [<a href="https://www.youtube.com/watch?v=B_8-B2rNw7s">listen here</a>]<br />
</p>

Of course, incorporating nonhuman agency is another way of relinquishing a degree of control over a finished result. Daniel Ranalli did this in a simple way with snails:

<p align="center">
  <img src="ranalli.jpg" width=500 /><br />
  Daniel Ranalli, <i>Double Line</i> (2007)<br />
</p>


### Digital

When it comes to computers, one way of generating random numbers is to measure some chaotic physical phenomena, like cosmic background radiation, and incorporating those numbers into a program. This can be done directly with sensors or via copying them from a published reference like [_A Million Random Digits_](https://www.youtube.com/watch?v=bvLD54GnOTk) which was created by the RAND corporation for this purpose in 1995.

A more clever way that we use today is a "pseudo-random number generator," an algorithm that takes a "seed" (like the current time) and [elaborates upon it](https://en.wikipedia.org/wiki/Mersenne_Twister). The resulting numbers are not strictly indeterminate as it is _possible_ to predict them, but for most purposes they are more than good enough. Many programming languages (including Python) include a function, usually called `random`, that lets us use these numbers.

Digital media artists have seized upon the opportunity to experiment. One example is [Harold Cohen](https://en.wikipedia.org/wiki/Harold_Cohen_(artist)) (1928–2016), who starting in the 1960s began developing an algorithm to make unique (though frequently representational) drawings using rules together with random parameters. He and others have made the specious claim that his program, which he called AARON, is an example of artificial intelligence—nonetheless, it demonstrates how powerful the random function can be.

<p align="center">
  <img src="aaron.jpg" width=500 /><br />
  Harold Cohen, painting by <i>AARON</i> (1995)<br />
</p>

A contemporary of Cohen's, Roman Verostko (1929–), approached indeterminacy with a very different aesthetic, even though his work similarly uses random parameters to craft form. The results reflect Verostko's mystic interest (and his time as a Benedictine monk). (Verostko also initiated the "[algorist](https://en.wikipedia.org/wiki/Algorithmic_art#Algorists)" movement of artists who work with computers.)

<p align="center">
  <img src="verostko.jpg" width=500 /><br />
  Roman Verostko, <i>FlyingCloud II</i> (1999)
</p>

[Casey Reas](https://en.wikipedia.org/wiki/Casey_Reas) (1972–), together with Ben Fry, is the creator of Processing. The application and library generalize many of the techniques used by earlier algorithmic artists, including `random`, which features prominently in Reas' own work.

<p align="center">
  <img src="reas.jpg" width=500 /><br />
  Casey Reas, <i>Process 18 (Software 2)</i> (2010)
</p>

Another notable artist who has used Processing goes by the name [LIA](https://en.wikipedia.org/wiki/Lia_(artist)). Her work often takes the form of animation, with infinitely evolving visuals that she performs live or which are displayed on a monitor within a frame.

<p align="center">
  <img src="lia.png" width=500 /><br />
  LIA, <i>Untitled 20160817</i> (2016)
</p>


## Code: Random parameters, loops, and `i`

How do these artists create such complex effects? While there is a lot of craft involved in their code, we can start to create visual artwork that operates similarly with just a few more techniques.

...but before we do anything else, let's take a second to talk about `print`.

```py
print(100)
```

Like the shape functions from Processing, `print` is a function that takes a parameter and does something with it. In this case, however, it doesn't draw anything to the canvas. Instead, it prints it out in Processing's console window:

<p align="center">
  <img src="canvas_0.png" width=500 /><br />
</p>

`print` ends up being a very useful function for [debugging](https://en.wikipedia.org/wiki/Debugging) our code, or at least getting a better sense of what's going on, as we will see.

### Random parameters

Now we're ready for `random`, which is also a function that takes a couple of parameters and produces a result. However, `random` doesn't draw anything to the canvas, either. Instead, it produces a random number within a given range.

```py
random(0, 100)  # a random number between 0 and 100
```

If you put this into a sketch, every time you run it, you'll get a different random number. But we can't see that number unless we print it out:

```py
print(random(0, 100))
```

Notice how we've put `random` _inside_ `print`. It can be tricky to keep track of all the parentheses, but this is a very useful thing to be able to do. `random` will first do its job and come up with a random number between 0 and 100, and then this number will be what `print` prints out. And every time the sketch is run, this number will be different. Try it.

<p align="center">
  <img src="canvas_1_.png" width=500 /><br />
</p>

Ok, so what can we do with this visually?

Let's start with a simple shape in the center of the canvas:

```py
size(500, 400)

circle(250, 200, 100) # x position, y position, diameter
```

<p align="center">
  <img src="canvas_2.png" width=500 /><br />
</p>

So far, we've only used static numbers for parameters in functions like `circle`. But what if we put random in there instead?

```py
size(500, 400)

circle(random(0, 500), random(0, 400), 100) # x position, y position, diameter
```

This looks a little weird with all the parentheses and commas (be careful to keep track of them all!), but all we've done is _substitute_ the static numbers that we were using with the `random` function and its parameters:
- `250` is replaced with `random(0, 500)`
- `200` is replaced with `random(0, 400)`

(We're using these particular parameters for `random` because they match the dimensions of the canvas, but in principle, they could be anything.)

The result is that every time you run this sketch, the circle will be drawn in a different location:


<p align="center">
  <img src="canvas_3.png" width=500 /><br />
</p>

How is that at all useful? Well, what if we repeated that random circle a bunch of times (and substituted the diameter with a random parameter too)?

```py
size(500, 400)

circle(random(0, 500), random(0, 400), random(10, 300))
circle(random(0, 500), random(0, 400), random(10, 300))
circle(random(0, 500), random(0, 400), random(10, 300))
circle(random(0, 500), random(0, 400), random(10, 300))
circle(random(0, 500), random(0, 400), random(10, 300))
circle(random(0, 500), random(0, 400), random(10, 300))
circle(random(0, 500), random(0, 400), random(10, 300))
circle(random(0, 500), random(0, 400), random(10, 300))
circle(random(0, 500), random(0, 400), random(10, 300))
circle(random(0, 500), random(0, 400), random(10, 300))
```

<p align="center">
  <img src="canvas_4.png" width=500 /><br />
</p>

This starts to get interesting. Each time you run the sketch, you'll have a different random composition.

However, it's also a bit tedious to write. What if we wanted 1000 circles? Too much typing. And this is where key programming structure can help us out: the _loop_.


### Loops

Loops in Python read like a statement in English about math:

```
For every integer called "i" in the range 0 to 10, do the following:
```

We just have to shorten it up a bit:

```py
size(500, 400)

for i in range(0, 10):
    circle(random(0, 500), random(0, 400), random(10, 300))
```

We'll come back to the meaning of `i`. For now, the key thing is that this loop repeats 10 times whatever is indented on the next line (or many lines) after the colon (indentation is another tricky thing you'll learn to keep track of).

That means this code is equivalent to the earlier example, but we've written it with just a few lines. On each iteration of the loop, the program chooses new random numbers for the parameters of `circle`.


<p align="center">
  <img src="canvas_5.png" width=500 /><br />
</p>

One thing that's helpful to note with `random` is that if the first parameter is 0, you can omit it. And note that `random` can be applied to color, not just shapes:
```py
# a random color with a random amount of opacity
fill(random(255), random(255), random(255), random(255))

# a random greyscale color with a random amount of opacity
fill(random(255), random(255))
```

Let's use this to make a somewhat more elaborate example:

```py
size(500, 400)

# no outline on the shapes
noStroke()

# repeat 100 times
for i in range(0, 100):

    # choose a random color   
    fill(random(255), random(255), random(255), random(255))  # choose random color and opacity

    # make a random triangle with the bounds of the canvas
    triangle(random(500), random(400), random(500), random(400), random(500), random(400))

```

<p align="center">
  <img src="canvas_6.png" width=500 /><br />
</p>

Now we're getting somewhere. If you play with the parameters, and add different shapes and colors, the complexity and richness will increase:

```py
size(500, 400)

# set the background to white
background(255, 255, 255)

# repeat everything 20 times
for i in range(0, 20):

    # make a random triangle with no outline and a random red-ish fill
    noStroke()
    fill(random(255), 0, 0, random(255))  # choose random color and opacity
    triangle(random(500), random(400), random(500), random(400), random(500), random(400))

    # make a circle with no fill and random greyscale outline of random weight
    noFill()
    stroke(random(255), random(255))
    strokeWeight(random(1, 10))
    circle(random(500), random(400), random(10, 50))
```

<p align="center">
  <img src="canvas_7.png" width=500 /><br />
</p>

 As you can see, even this relatively straightforward example shares a certain aesthetic with that of artists who work with indeterminacy that we've already seen. 

#### `i`


`i` is a **variable**. We'll be talking more about variables throughout the course, but for now suffice to say that `i` represents a different number for every iteration of the loop.





## Sketch #2

use regularity and irregularity together
