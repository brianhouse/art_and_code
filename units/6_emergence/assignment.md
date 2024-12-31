## Sketch #6: Emergence

### Preamble

Seeking and avoiding; adding, removing, re-positioning, and modifying agents. From these relatively simple building blocks, we can design micro-worlds with their own emergent behaviors. Note that the only time we use `random()` is to set the initial attributes of agents when they are created, yet their exact paths are entirely unpredictable. This makes our simulations examples of chaotic systems with a high sensitivity to initial conditions.

As humans, we are experts at making sense of complexity through narrative. Materially, what we have here are lots and lots of calculations updating the positions of circles. But it is almost impossible for us not to personify these circles as characters with particular drives. This is how video games work, of course, as well as animation in general.

When we personify, we impose all sorts of biases and expectations. This is what makes building a simulation an artistic exercise. In the demo, I've reproduced a predator/prey dynamic that we might recognize from nature but which also might be a mischaracterization of what actually happens in the natural world. Simulations like this are necessarily reductions, and the parameters we choose will effect how people receive the result.

### Assignment

Create a virtual micro-world that demonstrates emergent behavior. Building from the examples, design interactions between several different types of agents and their environment that produces a compelling and unpredictable result. Be deliberate about how you characterize your agents and their purposes; whether you simulate human or animal interaction or makes something entirely abstract, you should have an overarching concept that takes into account the biases and narrative power of simulation. Aim for your microworld to be self-sustaining—ie, it should not collapse or explode right away, but should continue to demonstrate interesting behavior as long as possible. At the same time, remember that your computer will have limits—the more agents and walls and behvaiors you have, the slower your computer may run.

Submit your code along with a [3-sentence statement](../../resources/statement_guidelines.md) as well as a 1-minute screen recording of the Processing window.

Information for making screen recordings:
- [MacOS](https://support.apple.com/guide/mac-help/take-a-screenshot-or-screen-recording-mh26782/mac)
- [Windows](https://betanews.com/2020/01/20/windows-10-screen-record-xbox-game-bar/)

### Code library

[agent_helper.py](emergence_demo/agent_helper.py)


### Code reference

### Walls

Constructor
```py
wall = Wall(x1, y1, x2, y2, thickness) # coordinates for the start and stop points of the line
                                       # thickness of the wall
```

NOTE: these parameters define the abstract "wall" for the purposes of the simulation physics. If you want to see it, you still have to draw it! The most basic wall:
```py
strokeWeight(wall.thickness)       
line(wall.x1, wall.y1, wall.x2, wall.y2)
```


### Agents

Constructor
```py
agent = Agent( x=pixels,            # start position x
               x=pixels,            # start position y
               draw=draw_function,  # name of custom function to use to draw the agent
               size=pixels,         # radius of the agent for collision purposes
               max_speed=velocity   # speed limit
               )
```

Properties of agents that can be referenced or changed
```py
agent.x
agent.y
agent.heading
```

Move the agent according to the physics of the simulation
```py
agent.move()
```

Establish the possibility of an agent colliding with other things
```py
agent.collide(other_agent)
agent.collide(list_of_agents)
agent.collide(a_wall)
agent.collide(list_of_walls)
```

Make the agent avoid other things
```py
agent.avoid(other_agent, threshold, strength)       # threshold is distance in pixels
agent.avoid(list_of_agents, threshold, strength)    # strength is between 0-1
agent.avoid(a_wall, threshold, strength)
agent.avoid(list_of_walls, threshold, strength)
agent.avoid_edges(threshold, strength)
```

Make it seek out other agents
```py
agent.seek(other_agent, threshold, strength)
agent.seek(list_of_agents, threshold, strength)
```

Tests for various situations
```py
agent.touching(other_agent) # returns True or False
agent.distance(other_agent) # returns distance in pixels
agent.closest(list_of_agents) # return the closest agent in the list
agent.is_visible(other_agent) # if the agent can "see" the other_agent (ie, not blocked by walls); returns True or False
```

Intervening
```py
agent.bump(direction_in_degrees, strength) # give the agent a bump
```


### Demo from class

```py
from agent_helper import *

def setup():
    global pig_list, robot_list, truffle_list, wall_list
    size(500, 500)
    
    # create 10 pigs and store them in the pig_list 
    pig_list = []    
    for i in range(10):    
        pig = Agent(x=random(width),
                    y=random(height),
                    draw=draw_pig,
                    size=20,      # this is used to compute the physics
                    max_speed=5,  # how fast can we go?
                    oinkiness=50) # you can make up variables 
        pig.bump(random(360), 1.0)# mix up the initial direction        
        pig_list.append(pig)
        
        
    robot_list = []
    for i in range(2):
        robot = Agent(x=random(width),
                      y=random(height),
                      draw=draw_robot,
                      size=30,
                      max_speed=2)
        robot.bump(random(360), 1.0)
        robot_list.append(robot)        
            
    truffle_list = []
    for i in range(2):
        truffle = Agent(x=random(width),
                      y=random(height),
                      draw=draw_truffle,
                      size=15,
                      max_speed=0)
        truffle.bump(random(360), 1.0)
        truffle_list.append(truffle)   
        
    wall_list = []
    for i in range(2):
        wall = Wall(100, height/2,   # start point x, y
                    width-100, height/2,   # end point x, y
                    thickness=20)         # thickness of the wall
        wall_list.append(wall)    
        
    
def draw():
    global pig_list, robot_list, truffle_list, wall_list
    background(255)    
    # draw a background
    # can be animated
    
    # draw all the walls in the wall list
    # (there's no special function like with Agents,
    # and you don't have to draw them if you don't want to see them)
    stroke(0)
    for wall in wall_list: 
        strokeWeight(wall.thickness)       
        line(wall.x1, wall.y1, wall.x2, wall.y2)  
        
            
    # every 100 frames add a truffle
    if frameCount % 100 == 0:        
        truffle = Agent(x=random(width), y=random(height), draw=draw_truffle, size=15, max_speed=0)
        truffle.bump(random(360), 1.0)
        truffle_list.append(truffle)        
        
    
    for pig in pig_list:
        pig.draw()
        pig.move()
        
        pig.collide(pig_list)
        pig.avoid_edges(50, 1)
        pig.collide(wall_list)
        
        pig.seek(pig_list, 200, .1)  # who, radius, strength
        pig.avoid(pig_list, 75, .2)
        pig.align(pig_list, 200, .1)
        
        # little pigs avoid the robots, big ones chase them
        if pig.size < 30:
            pig.avoid(robot_list, 300, 1)
        else:
            pig.seek( pig.closest(robot_list), 200, 1)
        
        pig.seek( pig.closest(truffle_list), 300, .8)
        for truffle in truffle_list:
            if pig.touching(truffle):
                truffle_list.remove(truffle)
                # let's put a max size on the pigs
                if pig.size < 100:
                    pig.size += 7
                

    for robot in robot_list:
        robot.draw()
        robot.move()
        
        robot.collide(wall_list)       
        robot.avoid_edges(50, 1)       
        robot.collide(robot_list)         
        
        robot.seek( robot.closest(pig_list) , 200, 1)        
        for pig in pig_list:
            if robot.touching(pig):
                # eat a little pig
                if pig.size < 30:
                    pig_list.remove(pig)
                # get eaten by a big one    
                else:
                    robot_list.remove(robot)

    # truffle doesn't do anything
    # although it could...                    
    for truffle in truffle_list:
        truffle.draw()


def draw_pig(pig):
    noStroke()
    # using ratios of pig size here so that
    # the pig can dynamically change size
    fill(245, 86, 222)
    circle(pig.x, pig.y, .7*pig.size)
    circle(pig.x, pig.y-(.34*pig.size), .5*pig.size)
    fill(0)
    circle(pig.x-3, pig.y-(.42*pig.size), 3)
    circle(pig.x+3, pig.y-(.42*pig.size), 3)
    strokeWeight(.06 * pig.size) 
    stroke(245, 86, 222)
    line(pig.x, pig.y, pig.x + swing(-5, 5, 20), pig.y+(.6*pig.size))
    
    
def draw_robot(robot):
    strokeWeight(2)
    stroke(200)
    fill(200)
    square(robot.x-15, robot.y-15, 30)
    fill(255, 0, 0)
    circle(robot.x - 10, robot.y - 10, 7)
    circle(robot.x + 10, robot.y - 10, 7)
    fill(255)
    circle(robot.x, robot.y + 8, swing(2, 15, 10))
    
    
def draw_truffle(truffle):
    fill(72, 42, 22)
    stroke(0)
    circle(truffle.x, truffle.y, 15)
```


### Another (similar) demo


```py
# import our helper code
from agent_helper import *

def setup():
    global bats, sharks, flowers, walls
    size(500, 500)

    # sometimes improves graphics
    pixelDensity(2)              
    
    # create an empty list
    bats = []             
    
    # we're going to make 20 bats and add them to the list              
    for i in range(20):
        
        # create an Agent object with custom attributes
        bat = Agent(x=random(width),   # start position x
                    y=random(height),  # start position y
                    draw=draw_bat,     # name of draw function which we will put below
                    size=5,            # radius for collisions
                    max_speed=5        # speed limit
                    )
        
        # add the bat to the list        
        bats.append(bat)
        
        # bump it in a random direction                 
        bat.bump(random(360), random(3)) 
        
    # same thing with sharks        
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
        
    # same thing with flowers
    flowers = []
    for i in range(2):
        flower = Agent(x=random(100, width-200), 
                       y=random(100, height-200), 
                       draw=draw_flower,
                       size=30,
                       max_speed=1,
                       nectar=255)
        flowers.append(flower)
            
    
    # make some walls
    walls = []
    for i in range(3):        
        wall = Wall(random(width), random(height),   # start point x, y
                    random(width), random(height),   # end point x, y
                    thickness=random(1, 20))         # how thick the wall is
        walls.append(wall)
                
    
def draw():
    global bats, sharks, flowers, walls
    background(255)
    fill(0)
    textSize(8)
    
    # draw the fps to the screen to monitor 
    text(int(frameRate), width-12, 10)

    # draw all the walls in the wall list
    for wall in walls: 
        strokeWeight(wall.thickness)       
        line(wall.x1, wall.y1, wall.x2, wall.y2)
                                                
    # for all the flowers in the flower list...        
    for flower in flowers:        
        flower.draw()  # draw using the function we supplied        
        flower.move()  # move it        
        flower.collide(walls) # a flower can collide with walls         
    
    # for all the flowers in the flower list...    
    for bat in bats:
        bat.draw()     # draw using the function we supplied 
        bat.move()     # move it
        bat.collide(bats)   # a bat can collide with other bats in the bat list
        bat.collide(walls)  # a bat can collide with the walls    
        bat.avoid(bats, 20, 1) # a bat avoids other bats if it's too close
        bat.seek(bats, 300, .3) # a bat seeks other bats
        bat.align(bats, 200, .3) # a bat aligns with other bats
        bat.seek(flowers, 500, .4) # a bat seeks flowers
        bat.collide(flowers)       # ...but can collide with them
        bat.avoid(sharks, 200, .75)  # it avoids sharks
        bat.avoid(walls, 30, 10)     # it avoids walls
        bat.avoid_edges(30, 10)      # it avoids the edges of the canvas
        
        # we're going to individually check every flower
        for flower in flowers:
            if bat.touching(flower): # is this bat touching this flower?
                flower.nectar -= 1 # reduce the flower's nectar
                if flower.nectar < 100: # is it too low on nectar?
                    flowers.remove(flower) # remove the flower
                    # make a new flower
                    flower = Agent(x=random(100, width-200), 
                                y=random(100, height-200), 
                                draw=draw_flower,
                                size=30,
                                max_speed=1,
                                nectar=255)
                    # add the new flower to the flowers list
                    flowers.append(flower)
                    
            
            
    for shark in sharks:        
        shark.draw()
        shark.move()
        shark.collide(walls)
        shark.collide(flowers)
        shark.avoid(walls, 20, 10) 
        shark.avoid_edges(20, 10)    
        
        # make the shark seek out the closest bat
        shark.seek(shark.closest(bats), 300, 1)
        
        # check all the bats individually
        for bat in bats:
            # is the shark touching this bat?
            if shark.touching(bat):
                # bye bye bat
                bats.remove(bat)
                       
                        
        
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
    
```

### Competing agents and carrying objects

```py
from agent_helper import *

def setup():
    global good_agent, evil_agent, food_list, target
    size(500, 500)
    
    # create two agents, one of them is evil
    good_agent = Agent(x=random(width),
                       y=random(height),
                       draw=draw_good_agent,
                       size=20,
                       food=False    # food that's being carried
                       )    
    
    evil_agent = Agent(x=random(width),
                       y=random(height),
                       draw=draw_evil_agent,
                       size=20,
                       food=False
                       )
                                
    food_list = []
    for i in range(10):
        food = Agent(x=random(width),
                     y=random(height),
                     draw=draw_food,
                     size=10
                     )
        food_list.append(food)
        
    target = Agent(x=width/2,
                   y=height/2,
                   draw=draw_target,
                   size=30
                   )        
        
def draw():
    global good_agent, evil_agent, food_list, target
    background(255)
           
    good_agent.draw()
    good_agent.move()
    good_agent.collide(evil_agent)
    good_agent.avoid(evil_agent, good_agent.size * 2, .8)
        
    # if the agent is not currently carrying food...
    if good_agent.food == False:           
        # the agent only want food within a certain range
        # so we create a new list
        # add all the food from food_list to it if it's in that range  
        good_food_list = []
        for food in food_list:
            if food.distance(target) > 50 and evil_agent.food != food:
                good_food_list.append(food)
        # seek the closest food in the good_food_list                            
        good_agent.seek(good_agent.closest(good_food_list), 400, .2)
        # pick up the food
        for food in good_food_list:
            if good_agent.touching(food):
                good_agent.food = food 
                
    # if the agent is currently carrying food...
    else:
        # move the food along with the agent
        good_agent.food.x = good_agent.x
        good_agent.food.y = good_agent.y
        good_agent.seek(target, 500, 1.0)
        if good_agent.distance(target) < 30:
            # drop the food
            good_agent.food = False                
                     
 
    ## now for the evil agent, with slightly different behaviors          
    evil_agent.draw()
    evil_agent.move()
    evil_agent.collide(good_agent)
    if evil_agent.food == False:           
        evil_food_list = []
        for food in food_list:
            if food.distance(target) < 50 and good_agent.food != food:
                evil_food_list.append(food)
        evil_agent.seek(evil_agent.closest(evil_food_list), 400, .2)
        for food in evil_food_list:
            if evil_agent.touching(food):
                evil_agent.food = food 
    else:
        evil_agent.food.x = evil_agent.x
        evil_agent.food.y = evil_agent.y
        evil_agent.avoid(target, 500, 1.0)
        if evil_agent.distance(target) > 200:
            evil_agent.food = False                                    
                                                                             
                                                        
    for food in food_list:
        food.draw()                   
            
        
    
def draw_good_agent(agent):
    fill(0, 0, 255)
    noStroke()    
    circle(agent.x, agent.y, agent.size)

def draw_evil_agent(agent):
    fill(255, 0, 0)
    noStroke()    
    circle(agent.x, agent.y, agent.size)
            
def draw_food(food):
    fill(0, 255, 0)
    noStroke()        
    square(food.x-food.size/2, food.y-food.size/2, food.size)    
    
def draw_target(target):
    fill(0, 255, 0)
    circle(target.x, target.y, target.size)
```


### Examples

<p>
  <img src="examples/em_nguyen_kid_soccer.gif" width="500" /><br />
  Em Nguyen, <i>Kid Soccer</i> (2023)<br />
</p>

<p>
  <img src="examples/molly_troxel_under_the_sea.gif" width="500" /><br />
  Molly Troxel, <i>Under the Sea</i> (2021)<br />
</p>

<p>
  <img src="examples/lauren_curry_woodland_ecosystem.gif" width="500" /><br />
  Lauren Curry, <i>Woodland Ecosystem</i> (2021)<br />
</p>
