// declare our array here
let balls

function setup() {

    // create a canvas that fills the browser window and attach it to your HTML
    createCanvas(windowWidth, windowHeight).parent('p5')
    // the p5 variables "width" and "height" hold the dimensions of the canvas

    // we have to do this here in order to use the random function
    balls = [   {   x: random(100, width-100),
                    y: random(100, height-100),
                    vx: random(5, 20),
                    vy: random(5, 20),
                    size: random(20, 100),
                    color: [random(255), random(100), random(100)],
                },
                {   x: random(100, width-100),
                    y: random(100, height-100),
                    vx: random(5, 20),
                    vy: random(5, 20),
                    size: random(20, 100),
                    color: [random(100), random(100), random(255)],
                },
                {   x: random(100, width-100),
                    y: random(100, height-100),
                    vx: random(5, 20),
                    vy: random(5, 20),
                    size: random(20, 100),
                    color: [random(100), random(255), random(100)],
                }
            ]

}

function draw() {

    background(255, 255, 200)

    for (let ball of balls) {

        // move the objects
        ball.x += ball.vx
        ball.y += ball.vy

        // draw the objects at the new location
        noStroke()
        fill(ball.color)
        circle(ball.x, ball.y, ball.size)

        // now update vx and vy for next time

        // add some gravity
        ball.vy += 0.2          // gravity!

        // bounce ball off walls (dampen with -.8 instead of -1)
        if (ball.x >= width - ball.size/2) {
            ball.vx *= -.8
            ball.x += ball.vx
        }
        if (ball.x <= 0 + ball.size/2) {
            ball.vx *= -.8
            ball.x += ball.vx
        }
        if (ball.y >= height - ball.size/2) {
            ball.vy *= -.8
            ball.y += ball.vy
        }
        if (ball.y <= 0 + ball.size/2) {
            ball.vy *= -.8
            ball.y += ball.vy
        }

        // check if it is colliding with another balls
        // let collisions = 0
        for (let other_ball of balls) {
            if (other_ball != ball) {   // don't compare with itself!

                // how close do they have to be to touch?
                let touching = abs(ball.size/2 + other_ball.size/2)

                // how far apart are they now?
                let distance = dist(ball.x, ball.y, other_ball.x, other_ball.y)

                // if theyre touching, bounce them
                // (not real physics, but close enough for now)
                if (distance <= touching) {
                    ball.vx *= -.8
                    ball.vy *= -.8
                    ball.x += ball.vx
                    ball.y += ball.vy
                }

            }
        }

    }

}

// if the window is resized, resize the canvas to match
function windowResized() {
    resizeCanvas(windowWidth, windowHeight)
}
