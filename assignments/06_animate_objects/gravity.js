// declare our array here
let bouncing_balls = []

function setup() {

    // create a canvas that fills the browser window and attach it to your HTML
    createCanvas(windowWidth, windowHeight).parent('p5')
    // the p5 variables "width" and "height" hold the dimensions of the canvas

    // loop 10 times
    // each time, create a random ball object
    for (let i=0; i<10; i++) {
        let random_ball = {     x: random(100, width-100),
                                y: random(100, height-100),
                                vx: random(5, 20),
                                vy: random(5, 20),
                                size: random(10, 100),
                                color: [random(255), random(255), random(255)],
                            }
        bouncing_balls.push(random_ball)
    }

}

function draw() {

    background(255, 255, 200)

    for (let ball of bouncing_balls) {

        // move the objects
        ball.x = ball.x + ball.vx + random(-4, 4)
        ball.y = ball.y + ball.vy + random(-4, 4)

        // draw the objects at the new location
        noStroke()
        fill(ball.color)
        circle(ball.x, ball.y, ball.size)

        // now update vx and vy for next time

        // add some gravity
        ball.vy = ball.vy + 0.2          // gravity!

        // bounce ball off walls (dampen by mulitplying by .8)
        if (ball.x >= width - ball.size/2) {
            ball.vx = -ball.vx * .8
            ball.x += ball.vx
        }
        if (ball.x <= 0 + ball.size/2) {
            ball.vx = -ball.vx * .8
            ball.x += ball.vx
        }
        if (ball.y >= height - ball.size/2) {
            ball.vy = -ball.vy * .8
            ball.y += ball.vy
        }
        if (ball.y <= 0 + ball.size/2) {
            ball.vy = -ball.vy * .8
            ball.y += ball.vy
        }

        // check if it is colliding with another ball
        // we do this by selecting a second ball from our array
        for (let other_ball of bouncing_balls) {
            if (other_ball != ball) {   // don't compare with itself!

                // how close do they have to be to touch?
                let touching = abs(ball.size/2 + other_ball.size/2)

                // how far apart are they now?
                let distance = dist(ball.x, ball.y, other_ball.x, other_ball.y)

                // if theyre touching, bounce them
                // (not real physics, but close enough for now)
                if (distance <= touching) {
                    ball.vx = -ball.vx * .8
                    ball.vy = -ball.vy * .8
                    ball.x = ball.x + ball.vx
                    ball.y = ball.y + ball.vy
                }

            }
        }

    }

}

// if the window is resized, resize the canvas to match
function windowResized() {
    resizeCanvas(windowWidth, windowHeight)
}
