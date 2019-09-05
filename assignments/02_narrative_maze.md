# Sketch #2: Narrative Maze

Using an online [BASIC interpreter](https://www.calormen.com/jsbasic/), create an interactive story (such as Zork) where the reader/interactor moves from one "room" to another using keyboard commands. For full credit, your program must demonstrate at least 5 different "rooms"; you may also want to have objects that can be carried between rooms and which have an effect on the narrative. 

### Example instructions

Print to the screen:  
`PRINT "HELLO WORLD`

Take input from the user:  
`INPUT A$`

Conditional logic:  
`IF A = "NORTH" GOTO 20`

Comparing strings:  
`LEFT$(A$, 2)` -- the two leftmost characters of A
`RIGHT$($A, 5)` -- the five rightmost characters of A
`MID$($A, 2, 1)` -- the third character of A

Other fun statements:
`INVERSE`
`NORMAL`
`FLASH`


One challenge working with BASIC is organizing your line numbers. You may want to reserve 100 line numbers for every state. 

For example:
```
100 PRINT "YOU ARE IN FIELDS 205. IT IS A DARK ROOM THAT SMELLS OF TROLLS. THERE ARE EXITS TO THE EAST AND WEST."
110 INPUT A$
120 IF A$ = "WEST" GOTO 200
125 IF A$ = "EAST" GOTO 300
130 PRINT "YOU CAN'T DO THAT HERE."
140 GOTO 110

200 PRINT "YOU ARE IN THE HALLWAY..."

300 PRINT "YOU ARE IN THE CLASSROOM..."
```


[BASIC Language Reference](https://www.apple.asimov.net/documentation/programming/basic/Applesoft%20BASIC%20Quick%20Reference%20Guide.pdf)


