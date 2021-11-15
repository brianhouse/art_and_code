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
    contain(agent, 0, 0, width, height, width*2)

def contain(agent, left=None, top=None, w=None, h=None, thickness=2000):
    velocity_x = cos(agent['heading']) * agent['speed']
    velocity_y = sin(agent['heading']) * agent['speed']
    if left is not None and -thickness < agent['x'] - left < 0:
        agent['heading'] = atan2(velocity_y, abs(velocity_x))
    if w is not None and -thickness < (left + w) - agent['x'] < 0:
        agent['heading'] = atan2(velocity_y, -abs(velocity_x))
    if top is not None and -thickness < agent['y'] - top < 0:
        agent['heading'] = atan2(abs(velocity_y), velocity_x)
    if h is not None and -thickness < (top + h) - agent['y'] < 0:
        agent['heading'] = atan2(-abs(velocity_y), velocity_x)


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
