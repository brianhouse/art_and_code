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
                    max_speed=5
                    )
        bats.append(bat)
        bat.bump(random(360), random(3))
        
    sharks = []
    for i in range(1):
        shark = Agent(x=random(width), 
                    y=random(height), 
                    draw=draw_shark,
                    size=10,
                    max_speed=3
                    ) 
        sharks.append(shark)
        shark.bump(random(360), random(3))  
        
    flowers = []
    for i in range(2):
        flower = Agent(x=random(100, width-200), 
                       y=random(100, height-200), 
                       draw=draw_flower,
                       size=30,
                       max_speed=1,
                       nectar=255)
        flowers.append(flower)
            
    
    walls = []
    for i in range(3):        
        wall = Wall(random(width), random(height), random(width), random(height), thickness=random(1, 20))
        walls.append(wall)
                
    
def draw():
    global bats, sharks, flowers, walls
    background(255)
    fill(0)
    textSize(8)
    text(int(frameRate), width-12, 10)
            
    for flower in flowers:
        flower.draw()
        flower.move()
        flower.collide(walls)
        
    for wall in walls: 
        strokeWeight(wall.thickness)       
        line(wall.x1, wall.y1, wall.x2, wall.y2)
    
    strokeWeight(1)
    for bat in bats:
        bat.draw()
        bat.move()
        bat.collide(bats)
        bat.collide(walls)      
        bat.avoid(bats, 20, 1)
        bat.seek(bats, 300, .3)
        bat.align(bats, 200, .3)
        bat.seek(flowers, 500, .4)
        bat.collide(flowers)
        bat.avoid(sharks, 200, .75)  
        bat.avoid(walls, 40, 1) 
        bat.avoid_edges(40, 1)
        for flower in flowers:
            if bat.touching(flower):
                flower.nectar -= 1
                if flower.nectar < 100:
                    flowers.remove(flower)
                    flower = Agent(x=random(100, width-200), 
                                y=random(100, height-200), 
                                draw=draw_flower,
                                size=30,
                                max_speed=1,
                                nectar=255)
                    flowers.append(flower)
                    
            
            
    for shark in sharks:        
        shark.draw()
        shark.move()
        shark.collide(walls)
        shark.collide(flowers)
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
    step = step_cycle(2, 6)
    if step == 0:
        line(bat.x, bat.y, bat.x + 5, bat.y + 10)
        line(bat.x, bat.y, bat.x - 5, bat.y + 10)
    elif step == 1:
        line(bat.x, bat.y, bat.x + 1, bat.y + 10)
        line(bat.x, bat.y, bat.x - 1, bat.y + 10)
    circle(bat.x, bat.y, bat.size)
    

def draw_shark(shark):
    strokeWeight(1)
    stroke(0)
    fill(255)
    step = step_cycle(2, 6)
    if step == 0:    
        line(shark.x, shark.y, shark.x + 10, shark.y + 20)
        line(shark.x, shark.y, shark.x - 10, shark.y + 20)
    else:
        line(shark.x, shark.y, shark.x + 3, shark.y + 20)
        line(shark.x, shark.y, shark.x - 3, shark.y + 20)    
    circle(shark.x, shark.y, shark.size)
    
    
def draw_flower(flower):
    strokeWeight(1)
    fill(flower.nectar, flower.nectar, 0)
    square(flower.x-10, flower.y-10, 20) 
    
    