# Sketch #8: Magic Mirror

Create a Magic Mirror that augments or replaces a person’s digital “reflection” with additional information or graphics.

Download [this template](08_magic_mirror.zip) to begin, which includes the [clmtracker library](https://github.com/auduno/clmtrackr) to identify the coordinates of key facial features. Incorporate these coordinates into abstract animation or use them as anchors for text or external images.

Your mirror should in some way address the relationship between our physical and digital identities.

### p5 template

```javascript
let capture
let tracker

function setup() {

    createCanvas(800, 600)

    // start capturing video
    capture = createCapture(VIDEO)
    capture.size(800, 600)
    capture.hide()

    // create the tracker
    tracker = new clm.tracker()
    tracker.init()
    tracker.start(capture.elt)    

}


function draw() {    

    background(0)
    
    // show the video feed
    image(capture, 0, 0, capture.width, capture.height)

    // get data from tracker
    let positions = tracker.getCurrentPosition()

    // make sure we have data to work with
    if (positions.length > 0) {

        stroke(255)
        fill(255)

        // draw the data
        let i = 0
        while (i < positions.length - 1) {
            ellipse(positions[i][0], positions[i][1], 4, 4)
            text(i, positions[i][0], positions[i][1])
            line(positions[i][0], positions[i][1], positions[i+1][0], positions[i+1][1])

            i += 1
        }

        // overlay eyes
        let leftEyeX = positions[32][0]
        let leftEyeY = positions[32][1]

        let rightEyeX = positions[27][0]
        let rightEyeY = positions[27][1]
        
        push()
        fill(255, 0, 0)
        ellipse(leftEyeX, leftEyeY, 20, 20)
        ellipse(rightEyeX, rightEyeY, 20, 20)
        pop()        

        // measure distances between features
        let noseX = positions[62][0]
        let noseY = positions[62][1]

        let leftNostrilX = positions[43][0]
        let leftNostrilY = positions[43][1]

        let rightNostrilX = positions[42][0]
        let rightNostrilY = positions[42][1]

        let distanceLeft = dist(noseX, noseY, leftNostrilX, leftNostrilY) 
        let distanceRight = dist(noseX, noseY, rightNostrilX, rightNostrilY)

        if (distanceLeft > distanceRight) {
            print('facing right')
        } else {
            print('facing left')
        }


    }

}

```


### Add a cheek point

```javascript
        let anchor1X = positions[39][0]
        let anchor1Y = positions[39][1]

        let anchor2X = positions[12][0]
        let anchor2Y = positions[12][1]

        let cheekX = (anchor1X + anchor2X) / 2
        let cheekY = (anchor1Y + anchor2Y) / 2
        fill(255, 100, 0)
        ellipse(cheekX, cheekY, 30, 30)
```        


### Darth Vader mask example with rotation

```javascript
let capture
let tracker

let darth

function preload() {

    darth = loadImage('darth.png')

}

function setup() {

    createCanvas(800, 600)

    // start capturing video
    capture = createCapture(VIDEO)
    capture.size(800, 600)
    capture.hide()

    // create the tracker
    tracker = new clm.tracker()
    tracker.init()
    tracker.start(capture.elt)    

}


function draw() {    

    background(0)
    
    // show the video feed
    image(capture, 0, 0, capture.width, capture.height)

    // get data from tracker
    let positions = tracker.getCurrentPosition()

    if (positions.length > 0) {  

        // define some reference positions for the nose and on either side of the face
        let noseX = positions[62][0]
        let noseY = positions[62][1]

        let bridgeX = positions[33][0]
        let bridgeY = positions[33][1]

        let faceLeftX = positions[1][0]
        let faceLeftY = positions[1][1]

        let faceRightX = positions[13][0]
        let faceRightY = positions[13][1]


        // measure the width of the face
        let face_width = dist(faceLeftX, faceLeftY, faceRightX, faceRightY)
        print(face_width)

        let ratio = darth.height / darth.width          // the aspect ratio of the image
        let w = face_width * 2                          // make darth's helmet a big bigger
        let h = w * ratio                               // define the height in terms of the width

  
        // get the angle of head tilt
        let v1 = createVector(bridgeX - noseX, bridgeY - noseY)
        let v2 = createVector(0, -100)
        let a = v2.angleBetween(v1)

        push()        
        translate(noseX, noseY) // rotate around the nose
        angleMode(DEGREES)
        rotate(a)
        image(darth, -w/2, -h/2, w, h)    // center the scaled image   
        pop()

        // draw the points for reference
        push()
        fill(0, 255, 0)
        ellipse(noseX, noseY, 10, 10)
        ellipse(bridgeX, bridgeY, 10, 10)
        ellipse(faceLeftX, faceLeftY, 10, 10)
        ellipse(faceRightX, faceRightY, 10, 10)
        line(faceLeftX, faceLeftY, faceRightX, faceRightY)
        line(noseX, noseY, bridgeX, bridgeY)
        pop()        


    }

}

```