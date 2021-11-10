## Sketch #8: Emergence

Create a virtual micro-world that demonstrates emergent behavior. Building from the examples, design interactions between several different types of agents and their environment that produces a compelling and unpredictable result. Be deliberate about how you characterize your agents and their purposes; whether you simulate human or animal interaction or makes something entirely abstract, you should have an overarching concept that takes into account the biases and narrative power of simulation.

Submit your code along with a [3-sentence description](../../resources/description_guidelines.md).


Avoid function:
```py
def avoid(agent, other, threshold, strength):
    if other == agent:
        return 0
    distance = dist(agent['x'], agent['y'], other['x'], other['y'])
    if distance < threshold:
        velocity_x = cos(agent['heading']) * agent['speed']
        velocity_y = sin(agent['heading']) * agent['speed']
        steer_x = ((agent['x'] - other['x']) / distance) * strength
        steer_y = ((agent['y'] - other['y']) / distance) * strength
        new_velocity_x = velocity_x + steer_x
        new_velocity_y = velocity_y + steer_y
        agent['heading'] = atan2(new_velocity_y, new_velocity_x)
    return distance
```

Wall function:
```py
def avoid_walls(agent, threshold, strength):
    walls = [{'x': 0, 'y': agent['y']}, {'x': 400, 'y': agent['y']}, {'x': agent['x'], 'y': 0}, {'x': agent['x'], 'y': 400}]
    for wall in walls:
        avoid(agent, wall, threshold, strength)   
```

Seek function:
```py
def seek(agent, other, threshold, strength):
    if other == agent:
        return 0
    distance = dist(agent['x'], agent['y'], other['x'], other['y'])
    if distance < threshold:
        velocity_x = cos(agent['heading']) * agent['speed']
        velocity_y = sin(agent['heading']) * agent['speed']
        steer_x = ((other['x'] - agent['x']) / distance) * strength      # this line reversed
        steer_y = ((other['y'] - agent['y']) / distance) * strength      # this line reversed
        new_velocity_x = velocity_x + steer_x
        new_velocity_y = velocity_y + steer_y
        agent['heading'] = atan2(new_velocity_y, new_velocity_x)
    return distance
```
