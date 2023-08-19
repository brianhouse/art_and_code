def setup():
    size(500, 400)
    pixelDensity(2)
    fill(0)   
    textSize(24)
    change_room(living_room) # function name given as argument 

def bedroom():
    text("Bedroom", 180, height/2)

def kitchen():
    text("Kitchen", 180, height/2)

def hallway():
    text("Hallway", 180, height/2)

def living_room():
    text("Living Room", 180, height/2)
 
    text("Go to kitchen", 20, height-100)
    kitchen_link = 20, height-120, width/3, 20
    draw_hotspot(kitchen_link)
    if check_hotspot(kitchen_link):
        change_room(kitchen)
    
    text("Go to hallway", width/2, height-100)
    hallway_link = width/2, height-120, width/3, 20
    draw_hotspot(hallway_link)
    if check_hotspot(hallway_link):
        change_room(hallway)

def bathroom():
    text("Bathroom", 180, height/2)
    
from nonlinearity_helper import *    
    
