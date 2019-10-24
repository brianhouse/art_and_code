# Sketch #7: Touch Instrument

## Part 1

Using [p5.sound](https://p5js.org/reference/#/libraries/p5.sound), create a mouse-controlled audio synthesizer. This is a similar sketch to your drawing tool--only with sound. Map the parameters of oscillators and envelopes to mouse movements and combine them to generate complex effects. Give visual feedback to reinforce for the user the sounds that are being made.


## Part 2

Adapt your touch instrument to your phone, tablet, or other mobile device. Use multi-touch gestures to take advantage of the greater expressivity of the touch screen. Additionally, incorporate preloaded samples into your instrument.


### HTML Template

```HTML
<html>

<head>
    <title>Instrument</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />    
    <script src="p5.js"></script>
    <script src="p5.sound.js"></script>    
    <script src="sketch_ref.js"></script>
    <style type="text/css">
        html, body {
            width: 100%;
            height: 100%;
            margin: 0;
            padding: 0;
            background-color: rgb(0, 0, 255);
        }
    </style>
</head>

<body>
    <div id="p5"></div>
</body>

</html>
```