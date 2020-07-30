
```py
size(500, 400)

circle(500/2, 400/2, 100) # center x, center y, diameter
```

It turns out that Python is very good at math. Here, instead calculating half of 500 ourselves and writing `250`, we write `500/2` and it calculates 250 for us.

Addition `+`, substraction `-`, multiplication `*`, and division `/` can all be used in this way.

That's not terribly useful on its own. But consider this:

```py
size(500, 400)

circle(width/2, height/2, 100) # center x, center y, diameter
```

Once again, this produces the same result. But what are `width` and `height`? They are shortcuts provided by Processing that represent the width and height of the canvas that we established with `size`. In this case, `width` equals 500, and `height` is 400. Using words like this to represent numbers is a type of **variable**, which we will talk about throughout the course.

What is useful about this is that now we can _substitute_ the static values of `500` and `400` in our code with `width` and `height`, respectively. And if we _change_ the values we give to `size`, we won't have to alter our code. `width/2` will always be the horizontal center of the canvas, no matter if the width is 500 or 1000.

```py
size(1000, 400)

circle(width/2, height/2, 100) # center x, center y, diameter
```

<p align="center">
  <img src="canvas_1.png" width=500 /><br />
</p>

This idea of _substitution_ is critical. Because it also lets us do something extraordinary. Consider this code:

```py
size(500, 400)

circle(width/2, height/2, random(10, 300)) # center x, center y, diameter
```
What happened to the parameter for the diameter of the circle? Previously, it was set to `100`. But now, it's `random(10, 300)` instead. The `random` function is being used as a _parameter_ for the `circle` function.

If you run this, it will draw a circle in the center of the canvas. But how big will it be?
