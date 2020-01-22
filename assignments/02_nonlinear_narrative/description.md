# Sketch #2: Nonlinear Narrative

When we watch TV or read a book, the story usually progresses in a linear way, from start to finish. But in life, the decisions we make affect the choices that are available to us. Digital Media allow for something in the middle: multiple stories can be told by providing points where the narrative branches via interaction.

With this sketch, you will create a text-based, nonlinear narrative where the reader/interactor chooses their path by inputting text. You may also want to have objects that can be "carried" and which have an effect on the narrative. While your work may be structurally similar to _Zork_, the content should reflect your own artistic concept. Review the links below for inspiration.

Requirements:
- Your program must demonstrate at least 5 different branching points that create meaningful alternative paths
- You must articulate your concept with a title and [3-sentence artist statement](resources/artist_statement_guidelines.md).


### Technical preparation

In this assignment, we will be getting familiar with a more fundamental way of interacting with the computer than its graphical user interface: text files and the terminal.

- Download and install [Atom](https://atom.io)
- Download install [Node](https://nodejs.org/en/download/)
- Download and unzip the [template](template.zip)
- Open the Terminal (`/Applications/Utilities/Terminal.app`) or Windows Command Prompt
- Change directories to the template folder by typing `cd`, space, and then dragging the folder to the Terminal window
- Run the example by typing `node example.js`


### Code

Perhaps the most fundamental programming structure is that of a _conditional_, commonly known as an `if` statement. We will be using [Javascript](https://en.wikipedia.org/wiki/JavaScript), and in this language, an `if` statement looks like this:

```

if (what is within these parentheses is true) {

	do this block of code

}

```

This is similar to the `repeat` command from the last sketch, and we can still think about it in terms of telling a "turtle" what to do--even if we aren't going to be drawing graphics and we won't see the turtle.

`if` can be paired with `else`:
```

if (what is within these parentheses is true) {

	do this block of code

} else {

	do this block instead

}

```

...and there is even `else if`:
```

if (what is within these parentheses is true) {

	do this block of code

} else if (what is within these parentheses is true) {

	do this block instead

} else {

	since neither are true, do this block

}

```

Keeping tracking of `()` and `{}` is going to be a major source of headaches in this course. Learn to love it.


### Technical references



### Conceptual references
- Jorge Luis Borges, [_The Garden of Forking Paths_](https://en.wikipedia.org/wiki/The_Garden_of_Forking_Paths) ([full text](https://archive.org/stream/TheGardenOfForkingPathsJorgeLuisBorges1941/The-Garden-of-Forking-Paths-Jorge-Luis-Borges-1941_djvu.txt))
Lynn Hershmann Leeson, _LORNA_



Important programming concepts: `if-then` conditionals, functions.


Book:
Shiffman: https://www.youtube.com/watch?v=1Osb_iGDdjk


https://www.w3schools.com/jsref/jsref_if.asp

https://blog.kadenze.com/creative-technology/telling-non-linear-narratives-through-code/
