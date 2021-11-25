from agent_helper import *

def setup():
    global bats, sharks, flowers, walls
    size(500, 500)
    pixelDensity(2)
    
    bats = []
    for i in range(20):
        bat = Agent(x=random(width), 
                    y=random(height), 
                    draw=draw_bat,
                    size=5,
                    speed=5
                    )
        bats.append(bat)
        bat.bump(random(360), random(3))
        
    sharks = []
    for i in range(1):
        shark = Agent(x=random(width), 
                    y=random(height), 
                    draw=draw_shark,
                    size=10,
                    speed=3
                    ) 
        sharks.append(shark)
        shark.bump(random(360), random(3))  
        
    flowers = []
    for i in range(0):
        flower = Agent(x=random(100, width-200), y=random(100, height-200))
        flowers.append(flower)
    
    walls = []
    for i in range(4):        
        wall = Wall(random(width), random(height), random(width), random(height), thickness=random(1, 20))
        walls.append(wall)
        
    
def draw():
    global bats, sharks, flowers, corners, walls
    background(255)
            
    for flower in flowers:
        strokeWeight(1)
        fill(255, 255, 0)
        square(flower.x-10, flower.y-10, 20) 
        
    for wall in walls: 
        strokeWeight(wall.thickness)       
        line(wall.x1, wall.y1, wall.x2, wall.y2)
    
    strokeWeight(1)
    for bat in bats:
        bat.draw()
        bat.move()
        bat.can_collide(bats)
        bat.can_collide(walls)      
        bat.avoid(bats, 20, 1)
        bat.seek(bats, 300, .3)
        bat.align(bats, 200, .3)
        bat.seek(flowers, 500, .4)
        bat.avoid(sharks, 200, .75)  
        bat.avoid(walls, 40, 1) 
        bat.avoid_edges(40, 1)
            
    for shark in sharks:        
        shark.draw()
        shark.move()
        shark.can_collide(walls)
        shark.seek(shark.closest(bats), 300, 1)
        for bat in bats:
            if shark.touching(bat):
                bats.remove(bat)       
        shark.avoid(walls, 50, 1) 
        shark.avoid_edges(50, 1)    
            
        
def draw_bat(bat):
    strokeWeight(1)
    fill(255)
    stroke(0)
    line(bat.x, bat.y, bat.x + 5, bat.y + 10)
    line(bat.x, bat.y, bat.x - 5, bat.y + 10)
    circle(bat.x, bat.y, bat.size)
    

def draw_shark(shark):
    strokeWeight(3)
    stroke(0)
    line(shark.x, shark.y, shark.x + 10, shark.y + 20)
    line(shark.x, shark.y, shark.x - 10, shark.y + 20)
    circle(shark.x, shark.y, shark.size)
    
    
def mouseClicked():
    for bat in bats:
        bat.bump(random(360), random(3))
