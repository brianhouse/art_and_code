# Nonlinearity

The focus of this unit will be on how to string together functions into nonlinear experiences. But before we get to that, let's introduce a few new materials to work with.


## Text

Processing has several built-in functions that allow us to put text on the canvas. The most basic is `text()`, which takes three arguments: the string itself, and an x and y coordinate for where to put the bottom-left corner of the text box. `fill()` designates the color (and the default is white). So to place black text in the upper left corner of our white canvas, we do the following:

```py
def setup():
    size(500, 400)
    pixelDensity(2) 
    
def draw():
    background(255) 
    fill(0)
    text("Hello World!", 0, 10)
```

(If your text looks ragged, try using `pixelDensity(2)`)

<p align="center">
  <img src="code/canvas_1.png" width=400 /><br />
</p>

#### Size

To change the size, we use `textSize()` (the default is 12):

```py
def setup():
    size(500, 400)
    pixelDensity(2) 

def draw():
    background(255)     
    fill(0)
    textSize(36)
    text("Hello World!", 0, 36)
```

<p align="center">
  <img src="code/canvas_2.png" width=400 /><br />
</p>

#### Alignment

To write from the center or the right, use `textAlign()`. This can be set to `LEFT`, `CENTER`, or `RIGHT`. 

```py
def setup():
    size(500, 400)
    pixelDensity(2) 

def draw():
    fill(0)
    textSize(36)
    textAlign(CENTER)
    text("Hello World!", width/2, height/2)
```

<p align="center">
  <img src="code/canvas_3.png" width=400 /><br />
</p>

#### Font

What is a font? A font is a particular size, style (normal, italic), and weight (bold, etc) of a given typeface, rendered as a file. Font formats include .ttf (TrueType) and .otf (OpenType), among others. Processing uses a built-in font by default; to change it, you'll need to download a .ttf or .otf file and add it to your sketch.

<!-- On a Mac, go to the Finder. Then choose "GO" –> "Library" from the menu bar while holding down "Option" (this makes the Library appear).  -->

How do you find a font? While fonts can be very expensive, many are available for free, such as from [https://www.1001freefonts.com](https://www.1001freefonts.com). When you download a typeface, you'll have a folder full of fonts of different variations.

<p align="center">
  <img src="code/canvas_4_font.png" width=500 /><br />
</p>

To add one of these to your sketch, use "Sketch" —> "Add File..." and navigate to a .ttf or .otf file.

<p align="center">
  <img src="code/canvas_5.png" width=300 /><br />
</p>

Once you do this, nothing will appear to have happened. However, if you do "Sketch" —> "Show Sketch Folder", you'll see that there is a "Data" folder inside it, and inside that, the font.

Next, we use the `createFont()` function to load it into Processing. This takes the filename of the font and a size, and it stores it in a variable. The size is more or less irrelevant, since we can change it later, but for best quality try to set it to approximately what you'll use—you can list more than one as additional arguments.

`createFont()` should always be called within `setup()`, but you can use `textFont()` anywhere to change fonts on the fly. Just keep in mind that you may need to make a global variable with the font name:

```py
def setup():
    global funky_font
    size(400, 300)
    pixelDensity(2)
    funky_font = createFont("KOMIKAB_.ttf", 36)

def draw():
    background(255)
    fill(0)
    textFont(funky_font)
    textSize(36)
    textAlign(CENTER)
    text("Hello World!", width/2, height/2)
```

<p align="center">
  <img src="code/canvas_6.png" width=400 /><br />
</p>


