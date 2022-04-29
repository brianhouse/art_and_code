## Organization

MORE SMALL GROUP DESK CRITS

## Units

Have explicit conceptual prompts each assignment. Must fulfill the tech thing (use a loop) and the conceptual aspect (sense of complexity... or whatever)


## repetition
add lovid

## recombination
have them do it first with scissors and paper?
more examples from students so they know the possibilities


## emergence

more for content on complex systems is here: https://natureofcode.com/book/chapter-6-autonomous-agents/

global function to turn on gravity

examples are a pin ball machine and the current shark thing

code reference with all the possibilities

agent.can_collide(other_agent)
agent.can_collide(list_of_agents)
agent.can_collide(a_wall)
agent.can_collide(list_of_walls)

integrate step cycle into objects and argument

conditionals
animation
walls
time

bug: initial Wall (have to put it in Agent constructor or something)

can_collide -> collides

calc heading function between two things? that let's them get in between the constraints, but also helps with the drawing.
it's particularly useful with the mouse

is heading flipped?
`beam.bump(degrees(beam.heading) + 180, 10)`
I think the rotation before drawing has to be 180 + heading or something

also: `velocity=laser_shark.velocity.copy()`
perhaps setting an initial heading is possible, and then can be bumped
yeah, that worked. so the issue is just the reversed heading, and the fact that agent.heading gives radians and not degrees. either fix that, or make bump take radians

need to have a "proposal" step where they come up with something

agents -> agent_list or all_agents
that's been a source of confusion

need a diagram for how to "draw" in the draw_agent functions


"speed" really makes more sense as "max_speed"

use bat.size




### general

- emphasize that the goal is to match concept and form
/

- still missing map(), seems significant


#####

## future

https://p5.readthedocs.io/en/latest/index.html


## visitors

Afroditi



## AC

- nonlinear narrative
- emergence
- glitch
