## Sketch #8: Emergence

Create a virtual micro-world that demonstrates emergent behavior. Building from the examples, design interactions between several different types of agents and their environment that produces a compelling and unpredictable result. Be deliberate about how you characterize your agents and their purposes; whether you simulate human or animal interaction or makes something entirely abstract, you should have an overarching concept that takes into account the biases and narrative power of simulation.

Submit your code along with a [3-sentence description](../../resources/description_guidelines.md).


### Helper code

Download [sim_helpers.py](sim_helpers.py) and add it to your sketch. Add this as your first line:

```py
from sim_helpers import *
```
You will then be able to use `avoid()`, `avoid_walls()`, and `seek()`.


### Interaction example

```py
from sim_helpers import *

def setup():
    global bees, flowers, sharks
    size(400, 400)

    bees = []
    for i in range(10):
        bee = {'x': random(400),
               'y': random(400),
               'heading': random(2 * PI),
               'speed': 1
               }
        bees.append(bee)

    flowers = []
    for i in range(3):
        flower = {'x': random(400),
                  'y': random(400)
                  }
        flowers.append(flower)

    sharks = []
    for i in range(3):
        shark = {'x': random(400),
                 'y': random(400),
                 'heading': random(2*PI),
                 'speed': 2,
                 'size': 10
                 }
        sharks.append(shark)


def draw():
    global bees, flowers, sharks
    background(255)

    for flower in flowers:            
        fill(255, 200, 200)
        square(flower['x'] - 5, flower['y'] - 5, 10)


    for bee in bees:

        fill(255, 255, 0)
        circle(bee['x'], bee['y'], 10)

        bee['x'] += cos(bee['heading']) * bee['speed']
        bee['y'] += sin(bee['heading']) * bee['speed']

        for other_bee in bees:
            avoid(bee, other_bee, 20, .5)

        for flower in flowers:
            seek(bee, flower, 50, .3)

        for shark in sharks:
            avoid(bee, shark, 100, .7)

        avoid_walls(bee, 10, 5)



    for shark in sharks:

        fill(255, 0, 255)
        circle(shark['x'], shark['y'], shark['size'])

        shark['x'] += cos(shark['heading']) * shark['speed']
        shark['y'] += sin(shark['heading']) * shark['speed']


        for other_shark in sharks:
            avoid(shark, other_shark, 20, .5)

        for bee in bees:
            distance = seek(shark, bee, 100, .5)
            if distance < 5:
                bees.remove(bee)
                shark['size'] += 3
                shark['speed'] -= .5

        avoid_walls(shark, 10, 5)

```

### Timer and random condition example
```py
from sim_helpers import *
from random import choice

def setup():
    global bees, flowers, season_timer, season   # add to globals
    size(400, 400)

    # set up timer variables
    season_timer = 0
    season = "spring"

    bees = []
    for i in range(10):
        bee = {'x': random(400),
               'y': random(400),
               'heading': random(2 * PI),
               'speed': 2
               }
        bees.append(bee)

    flowers = []
    for i in range(0):
        flower = {'x': random(400),
                  'y': random(400),
                  'color': color(255, 0, 0),
                  }
        flowers.append(flower)


def draw():
    global bees, flowers, season_timer, season  # add to globals
    background(255)

    # change the season        
    if millis() - season_timer > 3000:    # 3 second interval        
        if season == "spring":
            season = "summer"                            
        elif season == "summer":
            season = "fall"
        elif season == "fall":                
            season = "winter"
        elif season == "winter":
            season = "spring"
        season_timer = millis()            # reset season_timer

    if season == "spring":
        # randomly add a new flower with a 5% chance each frame        
        if random(100) < 5:                     
            flower = {'x': random(400),
                    'y': random(400),
                    'color': color(random(100, 255), random(100, 255), random(100, 255))
                    }
            flowers.append(flower)

    if season == "fall":
        # randomly wither a flower with a 50% chance each frame
        if random(100) < 50:  
            flower = choice(flowers)
            flower['color'] = color(255, 200, 0)                        

    if season == "winter":
        # randomly remove a flower with a 50% chance each frame
        if random(100) < 50 and len(flowers) > 0:
            flower = choice(flowers)
            flowers.remove(flower)


    for flower in flowers:            
        fill(flower['color'])
        square(flower['x'] - 5, flower['y'] - 5, 10)

    for bee in bees:
        fill(255, 255, 0)
        circle(bee['x'], bee['y'], 10)
        bee['x'] += cos(bee['heading']) * bee['speed']
        bee['y'] += sin(bee['heading']) * bee['speed']
        for other_bee in bees:
            avoid(bee, other_bee, 10, .5)
        for flower in flowers:
            seek(bee, flower, 50, .3)
        avoid_walls(bee, 10, 5)

```

### Animation example
```py
from sim_helpers import *

def setup():
    global bees, flowers, sharks
    size(400, 400)

    bees = []
    for i in range(10):
        bee = {'x': random(400),
               'y': random(400),
               'heading': random(2 * PI),
               'speed': 1
               }
        bees.append(bee)

    flowers = []
    for i in range(3):
        flower = {'x': random(400),
                  'y': random(400)
                  }
        flowers.append(flower)

    sharks = []
    for i in range(3):
        shark = {'x': random(400),
                 'y': random(400),
                 'heading': random(2*PI),
                 'speed': 2,
                 'size': 20
                 }
        sharks.append(shark)


def draw():
    global bees, flowers, sharks
    background(255)


    for flower in flowers:            
        fill(255, 200, 200)
        square(flower['x'] - 5, flower['y'] - 5, 10)


    for shark in sharks:

        # position takes an agent dictionary and a function that draws that object
        position(shark, draw_shark)

        shark['x'] += cos(shark['heading']) * shark['speed']
        shark['y'] += sin(shark['heading']) * shark['speed']

        for other_shark in sharks:
            avoid(shark, other_shark, 20, .5)

        for bee in bees:
            distance = seek(shark, bee, 100, .5)
            if distance < 5:
                bees.remove(bee)

        avoid_walls(shark, 10, 5)


    for bee in bees:

        # position takes an agent dictionary and a function that draws that object
        position(bee, draw_bee)

        bee['x'] += cos(bee['heading']) * bee['speed']
        bee['y'] += sin(bee['heading']) * bee['speed']

        for other_bee in bees:
            avoid(bee, other_bee, 20, .5)

        for flower in flowers:
            seek(bee, flower, 50, .3)

        for shark in sharks:
            avoid(bee, shark, 100, .7)

        avoid_walls(bee, 10, 5)        



def draw_shark(shark):

    step = step_cycle(2, 20) # two steps with a 20 frame delay

    stroke(0)
    fill(100, 100, 255)
    triangle(10, 0, -shark['size'], 10, -shark['size'], -10)

    if step == 0:
        fill(255)
        ellipse(-5, 0, 10, 10)    
        triangle(-10, 0, -2, -4, -2, 4)

    elif step == 1:
        fill(255)
        ellipse(-5, 0, 5, 10)    



def draw_bee(bee):

    step = step_cycle(2, 2) # two steps with a 2 frame delay

    stroke(0)
    fill(255, 255, 0)
    ellipse(0, 0, 20, 8)
    fill(0)
    circle(0, 0, 8)
    fill(255)

    if step == 0:        
        circle(2, -5, 8)
        circle(2, 5, 8)
```


### Wall example (may need to re-download sim_helpers.py)
```py
from sim_helpers import *

def setup():
    global agents, walls
    size(200, 200)
    agents = []
    for i in range(3):
        agent = {'x': random(200),
                 'y': random(200),
                 'heading': random(2*PI),
                 'speed': 3
                 }
        agents.append(agent)

    walls = []
    walls.append({'x': 100, 'y': 30, 'length': 140, 'direction': 'vertical'})
    walls.append({'x': 30, 'y': 100, 'length': 140, 'direction': 'horizontal'})


def draw():
    global agents, walls
    background(255)

    # draw some walls
    line(100, 30, 100, 170)
    line(30, 100, 170, width/2)


    for agent in agents:
        strokeWeight(1)
        circle(agent['x'], agent['y'], 20)

        agent['x'] += cos(agent['heading']) * agent['speed']
        agent['y'] += sin(agent['heading']) * agent['speed']

        # avoid the other agents (or bounce off of them)
        for other_agent in agents:
            avoid(agent, other_agent, 20, 1)

        # avoid the custom walls
        for wall in walls:                
            avoid_wall(agent, wall, 12, 5)

        # avoid the default walls around the edge of the canvas
        avoid_walls(agent, 10, 10)
```        
