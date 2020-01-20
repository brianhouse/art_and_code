# Sketch #1: Still Life for Turtle

A computer program is a set of instructions, or a "score," that is interpreted by a computer instead of a human. As humans, we intuitively rely on a common context to understand what is being said to us. Lacking this, a computer depends on us using an unambiguous formal language—aka code——that it knows how to interpret. 

For this sketch, you will give instructions to a "[turtle](https://brianhouse.github.io/turtle5/)" who will draw on the screen. This time, you will draw a [still life](https://en.wikipedia.org/wiki/Still_life) from the model in the room.

Requirements:
- Email your finished (or unfinished) code to the professor along with an image of your result

### Code

The turtle understands instructions like these:
- `forward(100)`    Move forward 100 steps (abbr: `fd`)
- `right(90)`     	Turn to the right 90º (abbr: `rt`)
- `left(90)`     	Turn to the left 90º (abbr: `lt`)
- `backwards(100)`  Move backwards 100 steps (abbr: `bk`)
- `penup()`        	Pull the pen up off the paper (abbr: `pu`)
- `pendown()`       Put the pen down on the paper (abbr: `pd`)
- `pencolor('red')` Change the color of the pen—note the quotes (abbr: `pc`)
- `penweight(5)`	Change the weight of the pen (abbr: `pw`)

Each of these instructions is known as a _function_—we can usually identify a function because it ends with a set of parentheses `()`. Often (but not always), the function takes an _argument_, such as the number of steps to move, the angle of the turn, or the name of the color.

In addition, the turtle can repeat instructions if they are enclosed by braces `{}`. The following code makes a square:
```
repeat(4) {  
  fd(100)
  rt(90)
}
```

`repeat` is a form of _loop_. And when code is surrounded by braces `{}`, it's called a _block_ of code.


\
To get the hang of things, have the turtle
- draw a square
- draw a triangle
- draw a circle (possible?)



#### Technical references

![](degrees.gif)


### Conceptual references

- [LOGO](https://en.wikipedia.org/wiki/Logo_(programming_language))
- [Harold Cohen and AARON](https://www.nytimes.com/2016/05/07/arts/design/harold-cohen-a-pioneer-of-computer-generated-art-dies-at-87.html)

