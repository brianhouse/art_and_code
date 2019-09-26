# Sketch #4: Digital Interpretation

Choose a [famous painting or other artwork from art history](https://www.google.com/search?q=famous+art) and reinterpret it in code using [p5](https://p5js.org). Abstract the original brushstrokes into geometric shapes, but retain a recognizable sense of the original composition. Pay particular attention to the use (or non-use) of color. Your interpretation should communicate something in its form that says something distinct from the original.

Your piece should be hosted on github—email a working URL (plus a link to the original artwork) to the professor before class.


### p5 Reference

Basic setup and drawing
```javascript
function setup() {

    // this is a comment

    createCanvas(500, 300)  // create a 400x300 canvas element

    angleMode(DEGREES)      // let's use degrees instead of radians

    noStroke()              
    fill(0, 0, 255)         // R G B values from 0-255 (google search: color picker)

    rect(0, 0, 500, 100)    // x, y, width, height
    rect(0, 200, 500, 300)

    fill(255, 0, 0)
    arc(200, 150, 200, 200, 25, 335)


    fill(255, 200, 0)
    ellipse(200, 150, 100, 100)   // center x, center y, radius width, radius height


    line(10, 150, 390, 150)  // x1, y1, x2, y2 (draws a line through center)


    noFill()
    stroke(0, 0, 0)          
    strokeWeight(5)         // thickness in pixels    
    rect(0, 0, 500, 300)

}


function mouseClicked() {                
    print(int(mouseX), int(mouseY))     // display coordinates of mouse click in js console
}

```

![p5 example](../img/CO.png?s=150)