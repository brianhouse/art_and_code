# Sketch #2: Narrative Maze

Using BASIC, create an interactive story (such as Zork) where the reader/interactor moves from one “room” to another using keyboard commands. For full credit, your program must demonstrate at least 10 different “rooms”; you may also want to have objects that can be carried between rooms and which have an affect on the narrative. 

Statements you’ll use:
`PRINT`
`IF`
`GOTO`
`INPUT`

One challenge working with BASIC is organizing your line numbers. You may want to reserve 100 line numbers for every state. 

For example:
```
100 PRINT “YOU ARE IN FIELDS 205. IT IS A DARK ROOM THAT SMELLS OF TROLLS. ...”
110 INPUT A$
120 IF A$ == “N” GOTO 200
130 PRINT “WHAT WAS THAT?”
140 GOTO 110

200 PRINT “YOU ARE IN THE HALLWAY...”
```
