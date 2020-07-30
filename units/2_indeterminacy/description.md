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


## Code: `random` parameters and `for` loops

How do these artists create such complex effects? While there is a lot of craft involved in their code, we can start to create visual artwork that operates similarly with just a few more techniques.

In the previous sketch, we created a shape using a function by defining its position with coordinates and giving numerical values for its other properties. For example, here's a circle in the center of the canvas:

```py
size(500, 400)

circle(250, 200, 100)
```

So far, we've only used static numbers for these parameters. However, Python can be more clever than that. For example, this code produces exactly the same result:

```py
size(500, 400)

circle(500/2, 400/2, 100)
```

It turns out that Python is very good at math. Here, instead of writing `250`, we write `500/2` and it calculates `250` for us. `/`, `*`, `+`, and `-` are all possibilities.

That's not terribly useful on its own. But consider this:

```py
size(500, 400)

circle(width/2, height/2, 100)
```

Once again, this produces the same result. But what are `width` and `height`? They are shortcuts provided by Processing that represent the width and height of the canvas that we established with `size`. They are also a type of variable.

What is useful about this is that now we can _substitute_ the static values of `500` and `400` in our code with `width` and `height`, respectively. And if we _change_ the values we give to `size`, we won't have to alter our code. `width/2` will always be the horizontal center of the canvas, no matter if the width is 500 or 10000.

This idea of _substitution_ is critical. Because it also lets us do something extraordinary. Consider this code:

```py
size(500, 400)

circle(width/2, height/2, random(10, 300))
```

If you run this, it will draw a circle in the center of the canvas. But how big will it be?




## Sketch #2
