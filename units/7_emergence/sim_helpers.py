def move(agent):
    agent['x'] += cos(agent['heading']) * agent['speed']
    agent['y'] += sin(agent['heading']) * agent['speed']

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


def avoid_walls(agent, threshold, strength):
    if agent['x'] < -threshold or agent['x'] > width + threshold or agent['y'] < -threshold or agent['y'] > height + threshold:
        agent['heading'] = atan2(agent['y'] - height/2, agent['x'] - width/2) * 180 / PI;
    else:
        walls = [{'x': 0, 'y': agent['y']}, {'x': width, 'y': agent['y']}, {'x': agent['x'], 'y': 0}, {'x': agent['x'], 'y': height}]
        for wall in walls:
            avoid(agent, wall, threshold, strength)


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


def position(agent, draw_f):
    pushMatrix()
    translate(agent['x'], agent['y'])
    rotate(agent['heading'])
    draw_f(agent)
    popMatrix()

def step_cycle(n, rate):
    return (frameCount / int(rate)) % n
