# Sketch #2: Nonlinear Narrative

When we watch TV or read a book, the story usually progresses in a linear way, from start to finish. But in life, the decisions we make affect the choices that are available to us. Digital Media allow for something in the middle: multiple stories can be told by providing points where the narrative branches via interaction.

With this sketch, you will create a text-based, nonlinear narrative using code where the reader/interactor chooses their path by inputting text. You may also want to have objects that can be "carried" and which have an effect on the narrative. While your work may be structurally similar to _Zork_, the content should reflect your own artistic concept.

Requirements:
- Before coding anything, draw a "map" of the the choices that will be available to your reader/interactor
- Your program must demonstrate at least 5 different branching points that create meaningful alternative paths
- You must articulate your concept with a title and [3-sentence description](resources/description_guidelines.md).

Email your title, concept, and code to the instructor. (You'll need to change the name of your file from `narrative.js` to `narrative.txt` in order to email it—otherwise Gmail will reject it)


## Conceptual references

### Pre-digital
- Jorge Luis Borges, [_The Garden of Forking Paths_](https://en.wikipedia.org/wiki/The_Garden_of_Forking_Paths) ([full text](https://archive.org/stream/TheGardenOfForkingPathsJorgeLuisBorges1941/The-Garden-of-Forking-Paths-Jorge-Luis-Borges-1941_djvu.txt))
- Raymond Queneau, [_A Hundred Thousand Billion Poems_](https://www.youtube.com/watch?v=2NhFoSFNQMQ)
- [Kinoautomat](https://monoskop.org/Kinoautomat)
- David Bowie's [verbasizer](https://www.vice.com/en_us/article/xygxpn/the-verbasizer-was-david-bowies-1995-lyric-writing-mac-app)

## Digital media
- [_ELIZA_](https://en.wikipedia.org/wiki/ELIZA)
- [_Zork_](https://en.wikipedia.org/wiki/Zork)
- Black Mirror, [_Bandersnatch_](https://en.wikipedia.org/wiki/Black_Mirror:_Bandersnatch)
- Lynn Hershmann Leeson, [_LORNA_](https://www.digitalartarchive.at/database/general/work/lorna.html)
- Lev Manovich, _Texas_


## Technical preparation

In this assignment, we will be getting familiar with a more fundamental way of interacting with the computer than its graphical user interface: text files and the terminal.

- Download and install [Atom](https://atom.io)
- Download install [Node](https://nodejs.org/en/download/)
- On MacOS, open the Terminal (`/Applications/Utilities/Terminal.app`) and practice navigating:
	- `pwd` shows the path of your current directory
	- `ls`  lists the content of your current directory
	- `cd`  followed by a space and a name changes to that directory
	- `cd ..`  moves backward into the enclosing directory
- On Windows, open the Command Prompt and practice navigating:
	- `D:`  changes to the D drive
	- `dir` lists the content of your current directory
	- `cd`  followed by a space and a name changes to that directory
	- `cd ..`  moves backward into the enclosing directory

Use your text editor to make a new file called `test.js` and type in the following:
```js
print = console.log

print('hello world!')
```

Save `test.js` on your desktop. Using the Terminal or Command Prompt, navigate to the desktop. Now type `node test.js`. Experiment with conditionals, functions, and variables as discussed below.

When you're ready to start this project:
- Download and unzip the [template](template.zip)
- Change directories to the template folder
- Run the example by typing `node example.js`
- Copy and paste the contents of `example.js` into a new file, called `narrative.js`, and save it in the same folder. You can then begin to modify the code to make your own nonlinear narrative.

## Code

### Conditionals

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

Keeping tracking of `()` and `{}` is going to be a major source of headaches in this course, but eventually you will internalize the structure and it will be easy to see if you've made a mistake.


### Functions

Functions are another way of organizing blocks of code. On the most fundamental level, functions allow you to reuse a block of code by giving it a name. In many cases, you'll use functions that have been written for you, such as `forward()` in the turtle exercise. But you can _declare_ your own functions using the `function` keyword, like this:

```js
function myFunctionName() {

	code goes here

}
```

`myFunctionName` could be anything, it's up to you to give the function a descriptive name. However, notice the parentheses after the function name—that's how you know it's a function. To _call_ your function—that is, to make it do its thing—you simply write its name with the parentheses, like this:

```js
myFunctionName()
```

Sometimes, functions _return_ a result, like this:
```js
let result = someFunction()
```
We won't get into how to do this yet, but when you see something like this, you know that the _variable_ `result` is now equal to whatever came out of `someFunction()`.

A what?


### Variables

A variable is just an arbitrary name for some value. It's like `x` in math. For example, you might use a variable called `name` to keep track of the user's first name so that you can use it later. Like functions, variables can be called whatever you want. But instead of using the word `function`, you use the word `let`, as in, "let the variable 'x' equal the value 6":
```js
let x = 6
```

### Putting it all together

Check out `example.js` in the template by opening it with your text editor (Atom). Here you'll see `if` statements as well as `function` declarations.

Every "room" of your narrative will consist of a function with the following form:

```js
// have a descriptive name for your function
function lobby() {

	// Start by describing what's going on
	print("You are in the lobby of the Art Department. A stairway leads upward, and a passage continues to the east. What do you want to do?")

	// Get a response from the interactor
	let response = prompt()

	// Depending on the response, call another function
	if (response.includes("passage")) {
		digitalMediaRoom()	// run the digitalMediaRoom function
	} else if (response.includes("east")) {
		digitalMediaRoom()	// run the digitalMediaRoom function
	} else if (response.includes("stairway")) {
		paintingRoom()	// run the paintingRoom function
	} else if (response.includes("up")) {
		paintingRoom()	// run the paintingRoom function
	} else {
		print("I don't understand.")

		// If the interactor types something unexpected, repeat this function		
		lobby()
	}

}
```
