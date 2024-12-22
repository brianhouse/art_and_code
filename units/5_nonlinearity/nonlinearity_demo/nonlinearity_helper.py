from __main__ import *

scene = None
previous_scene = None
f_changed = 0
pmousePressed = False

try:
    main_draw = draw
except NameError:
    main_draw = None

def draw():
    global pmousePressed
    background(255)
    if scene is not None:
        if not callable(scene):        
            raise Exception("change_scene() got a " + str(type(scene)).split("'")[1].split('.')[-1] + " instead of a function. Do two variables have the same name?")
        scene()
    if main_draw is not None:
        main_draw()
    pmousePressed = mousePressed        

def draw_hotspot(hotspot):
    push()
    noFill()
    strokeWeight(1)
    stroke(0, 255, 0)
    rect(*hotspot)
    pop()        
    
def click():
    return mousePressed != pmousePressed and not mousePressed    
    
def check_hotspot(hotspot, y=None, w=None, h=None):
    if not click():
        return False 
    if len(hotspot):
        x, y, w, h = hotspot
    return mouseX > x and mouseX < x + w and mouseY > y and mouseY < y + h
  
def change_scene(s):
    global scene, previous_scene, f_changed
    previous_scene = scene
    scene = s
    f_changed = frameCount
    
def go_back():
    change_scene(previous_scene)
    
def has_elapsed(duration):
    return frameCount - f_changed >= duration

def frame_changed():
    return f_changed    
    
def change(start, stop, duration, offset=0):
    return map((frameCount + offset) % max(duration, 1), 0, duration, start, stop)

def swing(start, stop, duration, offset=0): 
    position = -cos(2 * PI * change(0, 1, duration * 2, offset)) * .5 + .5
    return (position * (stop - start)) + start 
    
def load_animation(*sources):
    frames = []
    for source in sources:
        frames.append(loadImage(source))
    def f(x, y, speed=1, looping=False):
        if speed > 1:
            speed = 1
        speed = int(1/speed)        
        index = (frameCount - f_changed)
        if looping:
            index %= len(frames) * speed
        index //= speed
        if index >= len(frames):
            index = len(frames) - 1
        image(frames[index], x, y)
    return f          
