# import our helper code
from agent_helper import *

def setup():
    global bat_list, shark_list, flower_list, wall_list
    size(500, 500)

    # sometimes improves graphics
    pixelDensity(2)              
    
    # create an empty list
    bat_list = []             
    
    # we're going to make 20 bat_list and add them to the list              
    for i in range(20):
        
        # create an Agent object with custom attributes
        bat = Agent(x=random(width),   # start position x
                    y=random(height),  # start position y
                    draw=draw_bat,     # name of draw function which we will put below
                    size=5,            # radius for collisions
                    max_speed=5        # speed limit
                    )
        
        # add the bat to the list        
        bat_list.append(bat)
        
        # bump it in a random direction                 
        bat.bump(random(360), random(3)) 
        
    # same thing with shark_list        
    shark_list = []
    for i in range(1):
        shark = Agent(x=random(width), 
                    y=random(height), 
                    draw=draw_shark,
                    size=10,
                    max_speed=3
                    ) 
        shark_list.append(shark)
        shark.bump(random(360), random(3))  
        
    # same thing with flower_list
    flower_list = []
    for i in range(2):
        flower = Agent(x=random(100, width-200), 
                       y=random(100, height-200), 
                       draw=draw_flower,
                       size=30,
                       max_speed=1,
                       nectar=255)
        flower_list.append(flower)
            
    
    # make some wall_list
    wall_list = []
    for i in range(3):        
        wall = Wall(random(width), random(height),   # start point x, y
                    random(width), random(height),   # end point x, y
                    thickness=random(1, 20))         # how thick the wall is
        wall_list.append(wall)
                
    
def draw():
    global bat_list, shark_list, flower_list, wall_list
    background(255)
    fill(0)
    textSize(8)
    
    # draw the fps to the screen to monitor 
    text(int(frameRate), width-12, 10)

    # draw all the wall_list in the wall list
    for wall in wall_list: 
        strokeWeight(wall.thickness)       
        line(wall.x1, wall.y1, wall.x2, wall.y2)
                                                
    # for all the flower_list in the flower list...        
    for flower in flower_list:        
        flower.draw()  # draw using the function we supplied        
        flower.move()  # move it        
        flower.collide(wall_list) # a flower can collide with wall_list         
    
    # for all the flower_list in the flower list...    
    for bat in bat_list:
        bat.draw()     # draw using the function we supplied 
        bat.move()     # move it
        bat.collide(bat_list)   # a bat can collide with other bats in the list of bats
        bat.collide(wall_list)  # a bat can collide with the walls    
        bat.avoid(bat_list, 20, 1) # a bat avoids other bats if it's too close
        bat.seek(bat_list, 300, .3) # a bat seeks other bats
        bat.align(bat_list, 200, .3) # a bat aligns with other bats
        bat.seek(flower_list, 500, .4) # a bat seeks flowers
        bat.collide(flower_list)       # ...but can collide with them
        bat.avoid(shark_list, 200, .75)  # it avoids sharks
        bat.avoid(wall_list, 30, 10)     # it avoids walls
        bat.avoid_edges(30, 10)      # it avoids the edges of the canvas
        
        # we're going to individually check every flower
        for flower in flower_list:
            if bat.touching(flower): # is this bat touching this flower?
                flower.nectar -= 1 # reduce the flower's nectar
                if flower.nectar < 100: # is it too low on nectar?
                    flower_list.remove(flower) # remove the flower
                    # make a new flower
                    flower = Agent(x=random(100, width-200), 
                                y=random(100, height-200), 
                                draw=draw_flower,
                                size=30,
                                max_speed=1,
                                nectar=255)
                    # add the new flower to the flower list
                    flower_list.append(flower)
                    
            
            
    for shark in shark_list:        
        shark.draw()
        shark.move()
        shark.collide(wall_list)
        shark.collide(flower_list)
        shark.avoid(wall_list, 20, 10) 
        shark.avoid_edges(20, 10)    
        
        # make the shark seek out the closest bat
        shark.seek(shark.closest(bat_list), 300, 1)
        
        # check all the bat_list individually
        for bat in bat_list:
            # is the shark touching this bat?
            if shark.touching(bat):
                # bye bye bat
                bat_list.remove(bat)
                       
                        
def mouseReleased():
    global bat_list
    for bat in bat_list:
        heading = get_heading(mouseX, mouseY, bat.x, bat.y)
        bat.bump(heading, 2)              
        
        
def draw_bat(bat):
    strokeWeight(1)
    fill(255)
    stroke(0)
    line(bat.x, bat.y, bat.x + swing(1, 5, 5), bat.y + 10)
    line(bat.x, bat.y, bat.x - swing(1, 5, 5), bat.y + 10)
    circle(bat.x, bat.y, bat.size)
    

def draw_shark(shark):
    strokeWeight(1)
    stroke(0)
    fill(255)        
    line(shark.x, shark.y, shark.x + swing(3, 10, 5), shark.y + 20)
    line(shark.x, shark.y, shark.x - swing(3, 10, 5), shark.y + 20)    
    circle(shark.x, shark.y, shark.size)
    
    
def draw_flower(flower):
    strokeWeight(1)
    fill(flower.nectar, flower.nectar, 0)
    square(flower.x-10, flower.y-10, 20) 
    
    
