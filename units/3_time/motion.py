def setup():
    size(600, 600)


def draw():
    background(255)
    circle(swing(25, width-25, 200), height/2, 50)


def change(start, stop, duration, offset=0):
    return map((frameCount + offset) % max(duration, 1), 0, duration, start, stop)


def swing(start, stop, duration, offset=0): 
    position = -cos(2 * PI * change(0, 1, duration * 2, offset)) * .5 + .5
    return (position * (stop - start)) + start
