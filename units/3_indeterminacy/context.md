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

<!-- ### Response

Describe another example of indeterminacy in the world. Provide a link if possible.
 -->


##### The introduction to coding with this unit is [here](code.md).
