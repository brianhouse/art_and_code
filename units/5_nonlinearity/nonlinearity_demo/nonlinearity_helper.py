from __main__ import *

room = None
previous_room = None
change_frame = 0
pmousePressed = False

try:
    main_draw = draw
except NameError:
    main_draw = None

def draw():
    global pmousePressed
    background(255)
    if room is not None:
        try:
            room()
        except TypeError as e:
            print("change_room() didn't get a function. Is it a name conflict with a hotspot?")
            exit()
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
  
def change_room(r):
    global room, previous_room, change_frame
    previous_room = room
    room = r
    change_frame = frameCount
    
def go_back():
    change_room(previous_room)
    
def elapsed(duration):
    return frameCount - change_frame >= duration
    
def change(start, stop, duration, offset=0):
    return map((frameCount + offset) % max(duration, 1), 0, duration, start, stop)

def swing(start, stop, duration, offset=0): 
    position = -cos(2 * PI * change(0, 1, duration * 2, offset)) * .5 + .5
    return (position * (stop - start)) + start  
    
    
    
