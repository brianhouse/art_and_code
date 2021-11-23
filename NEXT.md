
Do small group screen sharing for intermediate feedback

## Organization

## Units

### coordinates
- bezier is impossible. need to show beginShape and curveVertex and have a mini-assignment on it
- definitely have beginShape endShape, also with regular shapes. the writing a letter thing was good
- had too much time, but that was because of labor time and canceled class

## indeterminacy
- not sure about the three versions thing. in some ways it worked, in some ways not, would have to emphasize that more. texture is a bit better
- might want to put the nature prompt back in?
- show how to draw a "soft line" with a loop of very random points over a very narrow band
- conceptual is really that randomness should play a role in the concept in some way

## nonlinearity
- make them make a toy example with three rooms and be strict about that so they don't immediately go off the deep end
- maybe outlaw "house" and fantasy adventure as themes, to break from Zork
- make them put title and description in the code itself
- spend more time on concept, has to be instruction about good gameplay or narrative for those to be meaningful grading points
    art: form matches content (maze of feelings, for example)
    game: what are the stakes?
    worldbuilding:
    immersion: meaningful choices
    maybe add additional "lecture": "On world-building", etc
    also aesthetics of the text
- map -> flowchart or diagram, otherwise they make a literal map
- have a whole section on text formatting
- have two rounds of playtesting
- have them present a concept in advance and have it critiqued
- the results were really too mechanical
- basically, get a lot more out of this assignment in terms of content and _design_--the code worked
- (also include "random" in there, which requires a different kind of import statement)
- this is such an absolute beast to grade (especially with two sections)

## recombination
/
sources:
books
wikipedia articles
transcribed audio
legal texts / laws / contracts
movies: scripts, closed-captioning
lyrics
newspaper articles
social media feeds

have them do it first with scissors and paper?

## glitch
Emphasize the error in transmission between source and result
use `source` as a variable in the code


## emergence
I'm wondering if we should just use objects instead of dictionaries.
If I'm cutting all the math down, it's structural anyway.
no-- it's too weird.
maybe?
```py
class Bat():
    def __init__(self, **properties):
        for key, value in properties.items():
            setattr(self, key, value)
```            
this could work, and would be nice, but it's a lot of hidden code.

- heading is not great. vectors are better, even if we don't use "Vector". ie, vx and vy make more sense because the avoid the trig. that's how I did it before. I dont know why Vector threw me off. then there's less hidden code.

- ok, actually this is not so bad. forget vectors. maybe pull distance out to be a separate function; that bit is confusing
- "strength" is the proportion of the new force to what's there

I guess the question is, if the functions are obscured anyway, why not use objects? then can still put the logic in the loop, I keep the logic in object.
```py
agent = Agent(x=5, y=10, heading=2*PI, draw=draw_bat)
...
agent.move()
for other_agent in agents:
    agent.avoid(other_agent)
```
I dont love that we lose the transparency of how animation works. can still do the initial demo. but we do get the joy of the dot.

bouncing off walls can be built in.
but then is it `draw_bat(agent)` ?
`agent.draw = draw_bat`
or put it in the constructor
(they could also override default functions that way)

but we still need
```py
agent.avoid(wall)
```
there, I did it. but it needs to be programmed all in vectors.

lifespan is a good use of timers
/
raise expecting Agent got list

seek avoid bounce

Agent
Wall

fix recombination to use word in words syntax

could have a list of vectors, and then combine them right before moving

obvi use vectors in the implementation



it's all just ifs, loops, variables, and lists

class Bat(Agent):

def draw(self):

def update(self):


is this better? with self? or is just doing it all in the loop better?

i think in the loop is actually going to be better

but it does mean separated draw_bat



at what point am i just teaching mindcraft?

i guess the difference is code itself



the key thing that is not understood is lists. Recombination didn't do that.


more for content on complex systems is here: https://natureofcode.com/book/chapter-6-autonomous-agents/


### general

obviously too much

- emphasize title and description—have them read it (and say nothing else?), and make sure it's good (synonymous with concept?)

- emphasize that the goal is to match concept and form

- add the new examples, natch!

- artist presentations -> survey presentations

- lectures are stumbling vs the notes. slides would be better.

- this should increasingly be about the _quality_ not the code. maybe this is a matter of adding a "design considerations" section after code or in each assignment

- it's really all about form matching content. that's what I care about.


/

- still missing map(), seems significant

//

Separate "Context", "Code", and "Concept" documents for each one? Concept being the design considerations to take into account when coming up with a concept and matching it to form?


next edition, go deeper on NN and simulation


### idea

eliminate recursion and recombination
move glitch before NN
then focus on simulation, with some mini list assignment first
this assumes simulation works well
alternately, really cut down recombination so it's not so much stupid syntax stuff:
load(text)
get_words(s)
get_sentences(s)
remove_punctuation(s)

examples:
sentence cut ups
interleave
find replace
sort analysis
free verse
madlibs


2D:
- coordinates
- repetition
- indeterminacy
- glitch

text:
- recombination / cut-ups, but make it simple
- narrative (use inventory)

simulation

interface



definitely zero on on those concept descriptions, maybe make it explicit that it's graded separately

flip the classroom: have them all review lecture notes as homework and come up with additional examples (will have to split code and context discussions)


#####

## future

https://p5.readthedocs.io/en/latest/index.html


## visitors

Afroditi
