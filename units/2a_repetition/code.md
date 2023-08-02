# Repetition

### Print

Before we get to repeating things, let's take a second to talk about `print()`, because it will help us understand what we're doing.

```py
print(100)
```

Like the shape functions from Processing, `print()` is a function that takes an argument and does something with it. In this case, however, it doesn't draw anything to the canvas. Instead, it prints it out in Processing's console window:

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

Got it? Great. But what the heck is `i`?

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
<p align="center">
  <img src="code/canvas_10.png" width=500 /><br />
</p>

This proves that our loop repeated, and that it did it ten times. Each time, `i` became a different number, which `print()` printed out. Notice, however, that we start with 0, not 1, and we end with 9, not 10. This seems counterintuitive at first, but it will end up making our lives simpler in many cases. From now on, just remember that computers start counting at 0, so you'll get all the numbers up to _but not including_ whatever number you give to `range()`.

## Drawing with Loops

Ok, so how is this helpful?

Consider the following code, which draws a series of vertical lines:

```py
size(360, 300)
background(255)
strokeWeight(10)

line(0, 0, 0, height)
line(40, 0, 40, height)
line(80, 0, 80, height)
line(120, 0, 120, height)
line(160, 0, 160, height)
line(200, 0, 200, height)
line(240, 0, 240, height)
line(280, 0, 280, height)
line(320, 0, 320, height)
line(360, 0, 360, height)
```
<p align="center">
  <img src="code/canvas_11_.png" width=360 /><br />
</p>

There is a lot of unnecessary labor in manually writing out all of these lines; furthermore, if we wanted to make a change, like making the lines slightly closer together, for example, we would have to edit every line.

Instead, let's use a `for` loop:
```py
size(360, 300)
background(255)
strokeWeight(10)    

for i in range(10):
    line(i * 40, 0, i * 40, height)    
```

You'll notice that this requires a bit of math. Until now, we've only supplied our drawing functions like `line()` with static numbers. But it turns out that Python can do math on the fly, so we can use short equations as arguments instead.

In this case, we give line a value of `i * 40` as the x-coordinate for both the start and the end of the line. We know that we are going to run this loop 10 times, and that `i` is going to begin as 0 and increase incrementally up until 9. `*` is the symbol for multiplication, so when we multiply those numbers by 40, we're going to get 0, 40, 80, 120, 160, 200, 240, 280, 320, 360 ... that means the lines will be in different places.

Try mixing it up a bit. Depending on how we replace the static numbers we're giving `line()` with multiples of i, we can get all sorts of results:

<!-- exercise: make them horizontal -->


```py
size(360, 300)
background(255)
strokeWeight(10)    

for i in range(10):
    line(180, 300, i * 40, 0)    
```

<p align="center">
  <img src="code/canvas_3.png" width=360 /><br />
</p>

```py
size(360, 300)
background(255)
strokeWeight(10)    

for i in range(10):
    line(i * 40, i * 10, i * 20, i * 30)    
```
<p align="center">
  <img src="code/canvas_2.png" width=360 /><br />
</p>

```py
size(360, 300)
background(255)
strokeWeight(10)    

for i in range(10):
    line(0, i * 15, width, i * 15)   
```
<p align="center">
  <img src="code/canvas_5.png" width=360 /><br />
</p>


```py
size(360, 300)
background(255)
strokeWeight(10)    

for i in range(10):
    line(i * 20, 0, (i * 20) + 180, height)    
```

<p align="center">
  <img src="code/canvas_4.png" width=360 /><br />
</p>

Notice how on this last example, the equation got a little more complicated: `(i * 20) + 180` uses parentheses to add 180 to the result after multiplying `i * 20`. There's a lot of expressive power in nesting operations like this.

Note that `i` can be used for other arguments besides coordinates:
```py
size(360, 300)
background(255)

for i in range(32):
    strokeWeight(i/3)
    line(0, i * 10, width, i * 10)     
```
<p align="center">
  <img src="code/canvas_6.png" width=360 /><br />
</p>

```py
size(360, 300)
background(255)

noFill()
for i in range(30):
    circle(180, 150, i * 10)  
```
<p align="center">
  <img src="code/canvas_19.png" width=360 /><br />
</p>



```py
size(360, 300)
background(255)
strokeWeight(5)

for i in range(256):
    stroke(200, i, 255)
    line(0, i + 45, width, i)
```
<p align="center">
  <img src="code/canvas_12.png" width=360 /><br />
</p>



### Nesting Loops

Let's make a row of circles:

```py
size(400, 300)
background(255)

for i in range(8):
    circle((i * 50) + 25, 25, 50)
```
<p align="center">
  <img src="code/canvas_13.png" width=400 /><br />
</p>

Here we have circles with a radius of 25 (and therefore a diameter of 50). By multiplying `i` by 50, we spread them out across the canvas. Since circles are drawn from the center, adding 25 shifts them over so we're not stuck with half a circle on the edge. So the x-coordinate becomes `(i * 50) + 25`.

So what do we do if we want to fill the canvas with circles? We need eight more rows. We could, of course, make eight separate `for` loops, with a different y-coordinate in each one. A better solution is to use _nested loops_:

```py
size(400, 300)
background(255)

for j in range(6):    
    for i in range(8):
        circle((i * 50) + 25, (j * 50) + 25, 50)
```
<p align="center">
  <img src="code/canvas_14.png" width=400 /><br />
</p>

The first thing to be careful of here is the indentation: we now have two levels.

Secondly, we have a new variable: `j`. We can actually name these variables whatever we want, `i` and `j` are just conventions, but they are helpful ones.

Since our canvas is 400 by 300 and our circles are 50 pixels in diameter, one of our loops repeats 6 times (300 / 50) and the other 8 times (400 / 50). We use equations with both `i` and `j` for the x- and y-coordinates that we give to circle. The computer does the rest.

Nesting loops like this can be used to create some interesting textures. Consider this basic unit:

```py
size(400, 300)
background(255)

line(0, 0, 10, 10)    
line(5, 15, 15, 5)    
```
<p align="center">
  <img src="code/canvas_16.png" width=400 /><br />
</p>

We're going to put these two lines inside of a nested `for` loop, and add either `(i * 15)` or `(j * 15)` to all the arguments. This will make the shape repeat and fill the canvas.

```py
size(400, 300)
background(255)

for j in range(40):    
    for i in range(40):
        line((i * 15) + 0, (j * 15) + 0, (i * 15) + 10, (j * 15) + 10)    
        line((i * 15) + 5, (j * 15) + 15, (i * 15) + 15, (j * 15) + 5)    
```
<p align="center">
  <img src="code/canvas_15.png" width=400 /><br />
</p>

From here, you might experiment with uneven increments:

```py
size(400, 300)
background(255)

for j in range(40):    
    for i in range(40):
        line(i * 14, j * 15, (i * 15) + 10, (j * 11) + 10)    
        line((i * 16) + 5, (j * 15) + 15, (i * 14) + 15, (j * 15) + 5)    
```
<p align="center">
  <img src="code/canvas_17.png" width=400 /><br />
</p>


Keep in mind that in all these examples, we've just used one loop (or a nested loop), but you might layer multiple loops together. And not everything has to be in a loop! Everything you've learned previously still applies.

```py
size(400, 300)
background(91, 206, 217)

stroke(183, 255, 0, 120)    
for j in range(31):    
    for i in range(41):
        line(200, 150, i * 10, j * 10)

stroke(255, 174, 0, 200)    
for j in range(12):    
    for i in range(16):
        line(200, 150, (i * 20) + 40, (j * 20) + 40)

noStroke()
fill(255, 0, 255)
for j in range(10):
    for i in range(10):
        circle((i * 6) + (j * 1.5) + 168, (j * 8) + (i * 2) + 110, 5)        
```

<p align="center">
  <img src="code/canvas_18_.png" width=400 /><br />
</p>


### `Map()`

In a previous example, we used i for both color values _and_ vertical pixels, iterating from 0–255 for both. In this case, it worked, but what if those ranges don't line up?

Consider this variation:

```py
size(360, 600)
background(255)

for i in range(height):
    stroke(i, 0, 255)
    line(0, i, width, i)
```    

<p align="center">
  <img src="code/canvas_20.png" width=360 /><br />
</p>

The gradient works, but only for the first 255 pixels—for the remaining 345 pixels, we're just stuck on magenta, because the red value for `stroke()` can't go any higher. How do we still use i but have `stroke()` progress through a different range?

This situation is a good candidate for using the `map()` function. What `map()` does is to take a variable like i along with information about its expected range and remap it to a different range.

```py
map(i, 0, height, 0, 255)   # variable, initial low, initial high, remapped low, remapped high
```

Unlike the functions we've seen so far, `map()` doesn't draw anything to the screen. Instead, it _returns_ a value. This means we can substitute this whole construction any time we use `i` in our code, but we want to remap its values. Like this:

```py
size(360, 600)
background(255)

for i in range(height):
    stroke(map(i, 0, height, 0, 255), 0, 255)  # i is replaced by map(i, 0, height, 0, 255)
    line(0, i, width, i)
```

This can look a little complicated with all the parentheses. But all we've done is to put `map()` inside of `stroke()` where `i` was before. The arguments we've given to `map()` are `i`, the low and high values we expect for `i` (which are 0 to height as determined by `range()`), and the low and high values we want for `stroke()` (0 and 255). Now, we get this:

<p align="center">
  <img src="code/canvas_21.png" width=360 /><br />
</p>

`map()` is not only useful for gradients. Anywhere you're using a loop and want to control two parameters at once it can come in handy. Here, we're mapping 100 circles so they are evenly distributed across the canvas (without doing any math!) and mapping the size so that those same 100 circles are distributed between a diameter of 1 and 200:

```py
size(360, 300)
background(255)

noFill()
for i in range(100):
    circle(map(i, 0, 100, 0, width), height/2, map(i, 0, 100, 1, 200))
```

<p align="center">
  <img src="code/canvas_22.png" width=360 /><br />
</p>
