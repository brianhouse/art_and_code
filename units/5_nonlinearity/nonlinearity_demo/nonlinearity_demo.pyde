def setup():
    size(500, 400)
    pixelDensity(2)
    fill(0)   
    textSize(24)
    change_scene(living_room) # function name given as argument 

def bedroom():
    text("Bedroom", 180, height/2)
    if has_elapsed(200):
        go_back()

def kitchen():
    text("Kitchen", swing(150, 210, 100), height/2)
    if has_elapsed(200):
        go_back()
    
def hallway():
    text("Hallway", 180, height/2)
    if has_elapsed(200):
        go_back()    

def living_room():
    text("Living room", 180, height/2)
 
    text("Go to kitchen", 20, height-100)
    kitchen_hotspot = 20, height-120, width/3, 20
    draw_hotspot(kitchen_hotspot)
    if check_hotspot(kitchen_hotspot):
        change_scene(kitchen)
    
    text("Go to hallway", width/2, height-100)
    hallway_hotspot = width/2, height-120, width/3, 20
    draw_hotspot(hallway_hotspot)
    if check_hotspot(hallway_hotspot):
        change_scene(hallway)

def bathroom():
    text("Bathroom", 180, height/2)
    
from nonlinearity_helper import *    
    
