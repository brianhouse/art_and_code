## Sketch #8: Emergence

Create a virtual micro-world that demonstrates emergent behavior. Building from the examples, design interactions between several different types of agents and their environment that produces a compelling and unpredictable result. Be deliberate about how you characterize your agents and their purposes; whether you simulate human or animal interaction or makes something entirely abstract, you should have an overarching concept that takes into account the biases and narrative power of simulation.

Submit your code along with a [3-sentence description](../../resources/description_guidelines.md).


### Helper code

Download [sim_helpers.py](sim_helpers.py) and add it to your sketch. Add this as your first line:

```py
from sim_helpers import *
```
You will then be able to use `avoid()`, `avoid_walls()`, and `seek()`.


### Example

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
    global bees, flowers
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
