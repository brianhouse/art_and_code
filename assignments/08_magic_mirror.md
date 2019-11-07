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