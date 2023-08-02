## Organization

SMALL GROUP DESK CRITS once the tables support it


### repetition

context: Walter Benjamin, Harold Cohen, NFTs, Steve Reich (micro effects emerge)

range parameters

op art -- more visual examples

coolers site for color schemes



### emergence

make .move() implicit?
add a function to move() to a given location ?
make a "rotate" property in the agent to adjust for drawing wrong

bounce vs wrap


note the need to have collides written first for wall visibility

- more background about what emergence is and the possibilities 

make the seek etc work with "cursor" or something


### interface

fill bucket using pixels


pMouse

agents

buttons that show if they are selected (in example)

drippy brush using agents (if after emergence)

using pgraphics could potentially avoid the painting over thing

fill bucket builds off of glitch?

bearing between mouse and pmouse 

circular buttons (in example)

have proper speed is important

need to use mouseReleased instead of mouseClicked

guassian example




### new nonlinear


interface introduces buttons and text, which is totally what is necessary for nonlinearity in this case, they're the same. how is nonlinearity going to be structured?

a function for each scene. but could be multiple parts as well.

if item_selected == True:
	showSection()

definitely turns into a game very quickly. 

nonlinearity could also use loaded images. maybe that's part of the assignment, to incorporate photos you take.

TheGameTheGame could be an example there.

this has to come after interface.


in this version, nonlinearity uses the same skillset as interface. introducing lists would be the thing. how does that fit? inventory, for one. maybe that's enough. and image could be introduced (that cuts down on the time spent drawing)

if statements become what's emphasized in interface. that's the point.

that's a little hard when we're also getting mouseX etc. variables aren't even necessary for time.


### setup


coordinates: basic drawing (need width/height)
rep+var: loops and random
time: events, frameCount, change and swing
interface: if! but also mouse..., and also variables? maybe can just emphasize brush as a variable. and make multiple variables that are True/False.




### format

the code lectures work well, I think I stick with my format

the context ones should be as discussion based as possible, could actually make sense to have slides
- just image slides
- bullet point concept slides

https://pandoc.org/MANUAL.html#synopsis

use HTML as an intermediate format, then I can style with css and outputs a pdf

just image with caption
for vids, straight link to github online
