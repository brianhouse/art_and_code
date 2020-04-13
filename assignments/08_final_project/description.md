# Final Project




## Example Code

### Setup for using external images in sketches

Because p5 runs in the browser, and because browsers have security restrictions that prevent it from accessing your files directly, there are a few extra steps if you want to load images directly in a p5 sketch. Specifically, you must run your sketch from a local web server. A "server" is simply a computer that provides access to a folder of files via HTTP—ie, the web. GitHub is already a server, so the following only applies to running your sketch locally. Once you've uploaded it, it should work as expected.

The p5 website outlines [a few ways to run a local server](https://github.com/processing/p5.js/wiki/Local-server).

The easiest is to install [Web Server for Chrome](https://chrome.google.com/webstore/detail/web-server-for-chrome/ofhbbkphhbklhfoeikjpcbhemlocgigb/).

When the extension is up and running, you'll point your browser at the URL showing on Chrome Web Server, which will look something like http://127.0.0.1:8887

Once that is all up and running, you'll be able to load images, sounds, and even videos into your sketches. For sound, you'll also need to have the p5.sound addon loaded. That happens in the HTML with another link to a script:

```html
<html>
  <head>
    <title>Loading Example</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.0.0/p5.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/p5.js/1.0.0/addons/p5.sound.js"></script>
    <script src="sketch.js"></script>
    <style type="text/css">
        html, body { margin: 0; padding; 0; }
    </style>
  </head>
  <body>
      <div id="p5"></div>
  </body>
</html>
```

And here's a `sketch.js` example of how to load an image, draw it at the mouse position, and play a sound effect when the mouse is clicked:

```js
let pio
let bark

function preload() {

    pio = loadImage("pio.jpg")
    bark = loadSound("bark.mp3")

}

function setup() {

    createCanvas(windowWidth, windowHeight).parent('p5')

}

function draw() {

    background(0)

    image(pio, mouseX, mouseY, pio.width, pio.height)

}

function mouseClicked() {

    bark.play()

}
```

Note that sounds cannot play automatically as soon as the sketch loads—this is another security feature of browsers that prevents advertisements from taking over your web experience. As long as the mouse has been clicked at least once (or the keyboard pressed), the sound can play.
