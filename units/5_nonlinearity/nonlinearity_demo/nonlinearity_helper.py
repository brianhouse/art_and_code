from __main__ import *

room = None
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
    
def check_hotspot(hotspot):
    if not click():
        return False
    x, y, w, h = hotspot
    return mouseX > x and mouseX < x + w and mouseY > y and mouseY < y + h
  
def change_room(r):
    global room
    room = r
    
