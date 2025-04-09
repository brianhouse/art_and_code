# Emergence

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
               y=pixels,            # start position y
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

## Simulation

Seeking and avoiding; adding, removing, re-positioning, and modifying agents. From these relatively simple building blocks, we can design micro-worlds with their own emergent behaviors. Note that the only time we use `random()` is to set the initial attributes of agents when they are created, yet their exact paths are entirely unpredictable. This makes our simulations examples of chaotic systems with a high sensitivity to initial conditions.

As humans, we are experts at making sense of complexity through narrative. Materially, what we have here are lots and lots of calculations updating the positions of circles. But it is almost impossible for us not to personify these circles as characters with particular drives. This is how video games work, of course, as well as animation in general.

When we personify, we impose all sorts of biases and expectations. This is what makes building a simulation an artistic exercise. In this example, I've reproduced a predator/prey dynamic that we might recognize from nature but which also might be a mischaracterization of what actually happens in the natural world. Simulations like this are necessarily reductions, and the parameters we choose will effect how people receive the result.

Part of the limits to simulation comes from the computational cost. What if we had 100 bats here? 1000? The code wouldn't change much at all. But if you try it, you'll notice your computer start to grind. This is really where supercomputers and cloud computation and quantum computing comes in—the capacity to do complex simulation. But there is always a limit.


