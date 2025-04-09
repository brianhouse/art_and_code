"""
Based on https://natureofcode.com/book/chapter-6-autonomous-agents/
https://flatredball.com/documentation/tutorials/math/circle-collision/
https://forum.processing.org/beta/num_1276644884.html
http://jeffreythompson.org/collision-detection/line-line.php
"""

import types, time
from random import choice

FRICTION = 0.005
MAX_FORCE = 0.1
BOUNCE = 0.75
GRAVITY = 0 #0.02


class Agent(object):
    
    
    def __init__(self, **properties):
        self.position = PVector(width/2, height/2)
        self.velocity = PVector(0, 0)
        self.acceleration = PVector(0, 0)
        self.size = 10
        self.max_speed = 1
        self._collisions = []
        self._walls = []        
        self._heading = 0.0
        for key, value in properties.items():
            setattr(self, key, value)
        if not len(Wall.walls):
            Wall(1, 0, 0, 0)            
            
            
    def __setattr__(self, key, value):
        if callable(value):
            if key == "draw":
                key = "_draw" 
            value = types.MethodType(value, self)
        object.__setattr__(self, key, value) 
    
             
    @property
    def x(self):
        return self.position.x    
        
        
    @x.setter
    def x(self, value):
        self.position.x = value


    @property
    def y(self):
        return self.position.y            
                  
                              
    @y.setter
    def y(self, value):
        self.position.y = value    
        
        
    @property
    def heading(self):
        if self.velocity.mag() > 0.01:
            self._heading = self.velocity.heading() + radians(90)
        return self._heading
            
        
    def move(self):        
        friction = self.velocity.get() * -1
        friction.setMag(FRICTION)  
        self.acceleration.add(friction) 
        if GRAVITY: 
            self.acceleration.add(PVector(0, GRAVITY)) 
        self.velocity.add(self.acceleration)        
        self.position.add(self.velocity)
        self.check_edges()        
        self.acceleration.mult(0)
        self._collisions = []  
        self._walls = []      

        
    def collide(self, entities):
        if type(entities) != list:
            entities = [entities]
        for entity in entities:
            if entity is None:
                continue            
            if type(entity) != Agent and type(entity) != Wall:
                raise Exception("Expecting Agent or Wall, got " + str(type(entity)))
            if type(entity) == Agent:
                self._resolve_agent_collision(entity)
            else:
                if entity not in self._walls:
                    self._walls.append(entity)
                self._resolve_wall_collision(entity)
            

    def _resolve_agent_collision(self, agent):
        if agent is self:
            return        
        distance = self.distance(agent)
        overlap = (self.size*.5 + agent.size*.5) - distance
        if overlap > 0:
            if self not in agent._collisions:
                self._collisions.append(agent) 
                mass_ratio = agent.size / float(self.size)
                tangent = PVector(agent.position.y - self.position.y, -(agent.position.x - self.position.x))  
                tangent.normalize()               
                 
                relative_velocity = (agent.velocity * mass_ratio) - self.velocity 
                tangent_velocity = tangent * relative_velocity.dot(tangent)
                self_collision = tangent_velocity - relative_velocity                      
                
                relative_velocity = agent.velocity - (self.velocity * (1.0/mass_ratio)) 
                tangent_velocity = tangent * relative_velocity.dot(tangent)
                agent_collision = tangent_velocity - relative_velocity                                                                      

                self.velocity.sub(self_collision)
                agent.velocity.add(agent_collision)   
                self.velocity.mult(BOUNCE)
                agent.velocity.mult(BOUNCE)             

                v = self.position - agent.position                
                v.setMag(overlap*.5)
                self.position.add(v)                
                
                v = agent.position - self.position
                v.setMag(overlap*.5)
                agent.position.add(v)
                        

    def _resolve_wall_collision(self, wall):
        p, distance = wall.intersection(self)
        overlap = (self.size*.5 + wall.thickness*.5) - distance            
        if overlap > 0:
            tangent = PVector(p.y - self.position.y, -(p.x - self.position.x))  
            tangent.normalize()        
            relative_velocity = -2.0 * self.velocity * BOUNCE
            tangent_velocity = tangent * relative_velocity.dot(tangent)
            self_collision = tangent_velocity - relative_velocity                      
            self.velocity.sub(self_collision)
            self.velocity.mult(BOUNCE)
            v = self.position - p                
            v.setMag(overlap)
            self.position.add(v)     

 
    def seek(self, agents, threshold, strength):
        strength = max(min(strength, 1.0), 0.0)                
        if type(agents) != list:
            agents = [agents]   
        if not len(agents):
            return                      
        sum = PVector(0, 0)
        count = 0
        for agent in agents:        
            if agent is None or agent is self or self.distance(agent) > threshold or not self.is_visible(agent):
                continue
            diff = agent.position - self.position
            diff.normalize()
            sum.add(diff)
            count += 1            
        if count > 0:
            sum.div(count)
            sum.setMag(self.max_speed)
            steer = sum - self.velocity
            steer.limit(MAX_FORCE)
            steer.mult(strength)
            self.acceleration.add(steer)
    
    
    def avoid(self, agents, threshold, strength):
        strength = max(min(strength, 1.0), 0.0)  
        if type(agents) != list:
            agents = [agents]
        if not len(agents):
            return                           
        if type(agents[0]) == Wall:
            return self._avoid_walls(agents, threshold, strength)
        sum = PVector(0, 0)
        count = 0
        for agent in agents:
            if agent is None or agent is self or self.distance(agent) > threshold or not self.is_visible(agent):
                continue
            diff = self.position - agent.position
            diff.normalize()
            sum.add(diff)
            count += 1            
        if count > 0:
            sum.div(count)            
            sum.setMag(self.max_speed)            
            steer = sum - self.velocity
            steer.limit(MAX_FORCE)
            steer.mult(strength)
            self.acceleration.add(steer)
            
            
    def _avoid_walls(self, walls, threshold, strength):
        sum = PVector(0, 0)
        count = 0
        for wall in walls:
            p, distance = wall.intersection(self)
            if wall is None or distance > threshold:
                continue
            diff = self.position - p
            diff.normalize()
            sum.add(diff)
            count += 1            
        if count > 0:
            sum.div(count)            
            sum.setMag(self.max_speed)            
            steer = sum - self.velocity
            steer.limit(MAX_FORCE)
            steer.mult(strength)
            self.acceleration.add(steer)
            
            
    def avoid_edges(self, threshold, strength):
        return self._avoid_walls(Wall.edges, threshold, strength)    
                    
                
    def align(self, agents, threshold, strength):
        strength = max(min(strength, 1.0), 0.0)                
        if type(agents) != list:
            agents = [agents]   
        sum = PVector(0, 0)
        count = 0
        for agent in agents:        
            if agent is None or agent is self or self.distance(agent) > threshold or not self.is_visible(agent):
                continue
            sum.add(agent.velocity)
            count += 1            
        if count > 0:
            sum.div(count)            
            sum.setMag(self.max_speed)            
            steer = sum - self.velocity
            steer.limit(MAX_FORCE)
            steer.mult(strength)
            self.acceleration.add(steer)                
                                                                            
    def touching(self, agent):
        return self.distance(agent) < self.size*.5 + agent.size*.5
        
        
    def distance(self, agent):
        if type(agent) != Agent:
            raise Exception("Expecting Agent, got " + str(type(agent)))
        return self.position.dist(agent.position)  
            
            
    def closest(self, agents):
        if type(agents) != list or (len(agents) and type(agents[0]) != Agent):
            raise Exception("Expecting list of agents")
        if not len(agents):
            return None
        return min(agents, key=lambda agent: self.distance(agent))                        
         

    def is_visible(self, agent):
        if type(agent) != Agent:
            raise Exception("Expecting Agent, got " + str(type(agent)))
        x1, y1 = self.position.x, self.position.y
        x2, y2 = agent.position.x, agent.position.y
        for wall in Wall.walls:
            if wall in self._walls:
                x3, y3 = wall.x1, wall.y1
                x4, y4 = wall.x2, wall.y2
                try:
                    uA = ((x4-x3)*(y1-y3) - (y4-y3)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))
                    uB = ((x2-x1)*(y1-y3) - (y2-y1)*(x1-x3)) / ((y4-y3)*(x2-x1) - (x4-x3)*(y2-y1))                        
                    if uA >= 0 and uA <= 1 and uB >= 0 and uB <= 1:
                        return False
                except ZeroDivisionError:
                    pass
        return True                    
                                                                               
    def check_edges(self):
        if self.position.x < self.size*.5:
            self.position.x = self.size*.5
            self.velocity.x = abs(self.velocity.x)
            self.velocity.mult(BOUNCE)
        if self.position.x > width - self.size*.5:
            self.position.x = width - self.size*.5
            self.velocity.x = -abs(self.velocity.x)
            self.velocity.mult(BOUNCE)
        if self.position.y < self.size*.5:
            self.position.y = self.size*.5
            self.velocity.y = abs(self.velocity.x)
            self.velocity.mult(BOUNCE)
        if self.position.y > height - self.size*.5:
            self.position.y = height - self.size*.5            
            self.velocity.y = -abs(self.velocity.x) 
            self.velocity.mult(BOUNCE)   
                                                                                                                                                                  

    def bump(self, deg, strength):
        x = cos(radians(deg) - radians(90)) * strength
        y = sin(radians(deg) - radians(90)) * strength
        bump = PVector(x, y)
        self.acceleration.add(bump)
  
  
    def draw(self):
        if self._draw is None:
            return
        pushMatrix()
        translate(self.x, self.y)
        rotate(self.heading)
        translate(-self.x, -self.y)
        self._draw()
        popMatrix()
                  
        
class Wall(object):
    
    edges = None
    walls = []
    
         
    def __init__(self, x1=0, y1=0, x2=0, y2=0, thickness=1):
        self.start = PVector(x1, y1)
        self.end = PVector(x2, y2)
        self.thickness = thickness
        self.update()
        Wall.walls.append(self)        
        if not Wall.edges:
            Wall.edges = True
            Wall.edges = [Wall(0, 0, width, 0),
            Wall(0, height, width, height),
            Wall(0, 0, 0, height),
            Wall(width, 0, width, height)
            ]  
            
            
    def __setattr__(self, key, value):
        if hasattr(self, key) and key in ['update', 'intersection']:
            raise Exception("Cannot override property " + key)
        object.__setattr__(self, key, value) 
                            
                
    @property
    def x1(self):
        return self.start.x    
        
        
    @x1.setter
    def x1(self, value):
        self.start.x = value
        self.update()


    @property
    def y1(self):
        return self.start.y            
                  
                              
    @y1.setter
    def y1(self, value):
        self.start.y = value  
        self.update() 
        
                
    @property
    def x2(self):
        return self.end.x    
        
        
    @x2.setter
    def x2(self, value):
        self.end.x = value
        self.update()


    @property
    def y2(self):
        return self.end.y            
                  
                              
    @y2.setter
    def y2(self, value):
        self.end.y = value 
        self.update()         
        
                                 
    def update(self):
        self.delta_x = self.x2 - self.x1
        self.delta_y = self.y2 - self.y1 
        self.length = sqrt(self.delta_x * self.delta_x + self.delta_y * self.delta_y) 
        self.cosine = self.delta_x / float(self.length)
        self.sine = self.delta_y / float(self.length)
        
        
    def intersection(self, agent):                
        p = PVector(0, 0)
        slope = (-self.x1 + agent.x) * self.cosine + (-self.y1 + agent.y) * self.sine
        if slope <= 0:
            p.x = self.x1 
            p.y = self.y1
        elif slope >= self.length:
            p.x = self.x2
            p.y = self.y2 
        else:
            p.x = self.x1 + slope * self.cosine 
            p.y = self.y1 + slope * self.sine 
        delta_x2 = agent.x - p.x 
        delta_y2 = agent.y - p.y
        return p, sqrt(delta_x2 * delta_x2 + delta_y2 * delta_y2)
        
             
    def destroy(self):
        if self in Wall.walls:
            Wall.walls.remove(self)
            
            
def get_heading(x1, y1, x2, y2):
    h = degrees(atan2(y2 - y1, x2 - x1)) - 90 + 180
    return h if h < 0 else h + 360

                        
def step_cycle(n, rate):
    return (frameCount / int(rate)) % n
    
    

def change(start, stop, duration, offset=0):
    if duration == 0:
        duration = 1    
    return map((frameCount - offset) % max(duration, 1), 0, duration, start, stop)


def swing(start, stop, duration, offset=0): 
    # duration is one half of the swing
    position = -cos(2 * PI * change(0, 1, duration * 2, offset)) * .5 + .5
    return (position * (stop - start)) + start
