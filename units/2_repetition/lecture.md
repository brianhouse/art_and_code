# Repetition

## Concept

Patterns are fundamental to both nature and human culture, and central to the idea of a pattern is the act of repetition. Computers are repetition specialists. Like many mechanical devices, they were invented in order to do something over and over again, quickly, in order exceed what what is possible by the human hand. When it comes to computation, the ability to take some logical possibility and enumerate it indefinitely undergirds much of the innovation digital media make possible.

Consequently, repeating patterns are central to digital aesthetics. Electronic music genres like techno are one obvious example; scrolling through endless posts on Instagram, playing a video game, or watching an animated movie all incorporate intense amounts of repetition. Digital media artists often use repetition explicitly in their work in order to highlight this aspect of computation.


## Context

### Non-digital

Predating digital technology, repeating patterns have been a part of the art and craft of every human culture. One particularly notable medium, of course, is textiles. Weaving on a loom involves an intricate manual or mechanical process in which horizontal threads are repeatedly interlaced at right angles to create fabric; geometric patterns are formed through variation in the method of weaving and the color of the threads used within a single cloth, designs for which are an important part of cultures' heritage.

<p align="center">
  <img src="context/1_cusco.jpg" width=500 /><br />
  Traditional Peruvian cloth from Cusco region, via <a href="https://en.wikipedia.org/wiki/Nilda_Callañaupa_Alvarez">Nilda Callañaupa Alvarez</a><br />
</p>

<p align="center">
  <img src="context/2_albers.jpg" width=500 /><br />
  Diagram showing weaving notation, <a href="https://en.wikipedia.org/wiki/Anni_Albers">Anni Albers</a>, <i>On Weaving</i> (1965)<br />
</p>

Weaving and looms are particularly important to the history of digital media. In fact, many people consider the Jacquard Loom to be the first computing device. Invented in France in 1804 by Joseph Marie Jacquard, this loom used punch cards to determine the pattern that was mechanically woven. This idea of representing data in a separate medium—the cards—which could then be reproduced repeatedly by a machine was a direct precursor to Charles Babbage's [Analytical Engine](https://en.wikipedia.org/wiki/Analytical_Engine), which operated similarly (though it enumerated logic, rather than fabric), and we've seen how early digital media artists like Lillian Schwartz encoded their visual designs into punch cards.

<p align="center">
  <img src="context/3_loom.jpg" width=500 /><br />
  Jacquard Loom<br />
</p>

The Jacquard Loom was emblematic of the [Industrial Revolution](https://en.wikipedia.org/wiki/Industrial_Revolution), a period spanning the turn of the 19th century that saw the mechanization of manufacturing processes and the reorganization of social relations to support capitalist enterprises. Industrialization began a process through which mass-production would transform all aspect of everyday life around the globe. By the 20th century, fine artists were incorporating and commenting upon such mechanisms in their work, such as the previously mentioned Bauhaus movement (see Annie Albers, above).

One particularly prominent figure in contemporary art in this regard is Andy Warhol (1928–1987). Identifying repetition as a central trope of modern society that had been largely ignored by the fine art world, Warhol and embraced mass-production techniques. Together with other artists associated with "[pop art](https://en.wikipedia.org/wiki/Pop_art)," he brought popular media, celebrity, and advertising into the art world vernacular.

<p align="center">
  <img src="context/4_warhol.jpg" width=500 /><br />
  Andy Warhol, <i>Campbell's Soup Cans</i> (1962)<br />
</p>

In reference to _Campbell's Soup Cans_, one of his most famous works, Warhol commented, "I used to have the same lunch every day, for twenty years, I guess, the same thing over and over again." And yet, Warhol is also known for the coining the phrase "15-minutes of fame" and for creating "screen tests" of his friends, anticipating social media and the influencer culture today.

Warhol's taste for rapid and vapid repetition contrasts another New York City-based artist of a subsequent generation who took industrial repetition in a completely different direction—Taiwanese artist Tehching Hsieh (1950–). One example is _One Year Performance 1980–1981 (Time Clock Piece)_, in which Hsieh punched a time clock and took a photograph of himself every hour on the hour for an entire year.

<p align="center">
  <img src="context/5_hsieh.jpg" width=500 /><br />
  Tehching Hsieh, <i>One Year Performance 1980–1981 (Time Clock Piece)</i> <br />
  <a href="https://www.youtube.com/watch?v=k4_xw2zyQN4">Full video here</a>
</p>

Hsieh's "durational performance" is at once at critique of the artificiality of mechanized time, an exploration of film as a medium that changes our experience of temporality, and a meditation on change with his own body as medium.

However, although Western industrialized society provides many precedents like these for understanding repetition in computation, a potent precursor in algorithmic visual design is Islamic art (in fact, [the word "algorithm" comes from the name of a Persian Mathematician](https://en.wikipedia.org/wiki/Algorithm#Etymology) from the ninth century, Muhammad ibn Musa al-Khwarizmi, who first developed algebra). In particular, incredibly ornate brick and tile geometry characterize the architectural facades of mosques in the years 800–1600, reflecting a religious commitment to avoid figurative artwork.

<p align="center">
  <img src="context/6_hafez.jpg" width=500 /><br />
  Tomb of Hafez, Shiraz, Iran
</p>

Many of these patterns are algorithmic in nature, where a simple set of shapes are repeated to generate rich complexity.

<p align="center">
  <img src="context/7_alhambra.jpg" width=500 /><br />
  Constructing patterns at Alhambra castle, Spain
</p>


### Digital

In the digital domain, many of the visual artists who first experimented with computers intuitively worked with the machine's inclination toward repetition while at the same time introducing variation. Hungarian artist Vera Molnár (born 1924 and still living) is a pioneer in this regard. Starting as early as the 1960s, Molnár used the programming languages Fortran and BASIC to control a pen-plotter machine, which is a robotic arm that holds a pen. These abstract images convey a tension between order and disorder (as her titles often suggest).

<p align="center">
  <img src="context/8_molnar.jpg" width=500 /><br />
  Vera Molnár, <i>(Des)Ordres</i> (1974)
</p>

Today, repetition is so ingrained with digital artists' work as to be somewhat difficult to pinpoint. It might be used to create an abstract pattern or a figurative texture, like hair, and consist of simple regular shapes or small components with unique characteristics. This example comes from Jared Tarbell, an early artist to find success using Processing. While organic-looking, it repeats a short algorithm over and over to create a twisted form.

<p align="center">
  <img src="context/9_tarbell.jpg" width=500 /><br />
  Jared Tarbell, <i>Guts</i> (2004)
</p>


## Code

### Print

Before we get to repeating things, let's take a second to talk about `print`, because it will help us understand what we're doing.

```py
print(100)
```

Like the shape functions from Processing, `print` is a function that takes a parameter and does something with it. In this case, however, it doesn't draw anything to the canvas. Instead, it prints it out in Processing's console window:

<p align="center">
  <img src="code/canvas_0.png" width=500 /><br />
</p>

`print` ends up being a very useful function for [debugging](https://en.wikipedia.org/wiki/Debugging) our code, or at least getting a better sense of what's going on, as we will see.



### `for` Loops

In programming, repetition is made much easier using loops. Check out the following code:

```py
for i in range(10):
    print(i)
```

There are several interesting things going on here. But because Python is English-like, we can almost read it as a sentence: _for every integer in a range up to 10, print out the number_.

Let's break it down:
- The key word here is `for`, which lets the computer know we're going to be repeating something.
- How many times are we going to repeat it? This is where `range()` comes in. Whatever number we give to range determines the number of repetitions.
- What are we going to be repeating? Whatever is _indented_ below the `for` command. In many programming languages, indentation doesn't matter, but in Python, it's very important.

Got it? Great. But what the hell is `i`?

`i` is a **variable**. That means `i` means something different each time the loop repeats. It's just like in math, where we'd typically use "x" to represent a number that might have an unknown value (actually, we could use "x" here too, but "i" is more common in programming so we don't get it mixed up with x/y spatial coordinates). So in this case, when we're repeating our loop 10 times, i is going to be a different integer up to 10.

Running the program, you should see this in the console:
```
0
1
2
3
4
5
6
7
8
9
```
This proves that our loop repeated, and that it did it ten times. Each time, `i` became a different number, which `print()` printed out. Notice, however, that we start with 0, not 1, and we end with 9, not 10. This seems counterintuitive at first, but it will end up making our lives simpler. From now on, just remember that computers start counting at 0, so you'll get all the numbers up to _but not including_ whatever number you give to `range()`.

Ok, so how is this helpful?
