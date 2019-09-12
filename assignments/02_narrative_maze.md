# Sketch #2: Narrative Maze

Using an online [BASIC interpreter](https://www.calormen.com/jsbasic/), create an interactive story (such as Zork) where the reader/interactor moves from one "room" to another using keyboard commands. For full credit, your program must demonstrate at least 8 different "rooms"; you may also want to have objects that can be carried between rooms and which have an effect on the narrative. 

### Example instructions

Clear the screen:
`HOME`  

Print to the screen:  
`PRINT "HELLO WORLD`

Take input from the user:  
`INPUT A$`

Conditional logic:  
`IF A$ = "NORTH" GOTO 20`  

Conditional logic with multiple possibilities:  
`IF A$ = "BLUE" OR A$ = "GREEN" GOTO 20`

Comparing strings:  
`IF LEFT$(A$, 2)` -- the two leftmost characters of A  
`RIGHT$($A, 5)` -- the five rightmost characters of A  
`MID$($A, 2, 1)` -- the second character of A  

Other fun statements:
`INVERSE`  
`NORMAL`  
`FLASH`  

Write a comment:
`REM THIS IS A COMMENT`


One challenge working with BASIC is organizing your line numbers. You may want to reserve 100 line numbers for every "room". 

For example:
```
0 HOME

100 REM FIELDS 205
100 PRINT "YOU ARE IN FIELDS 205. IT IS A DARK ROOM THAT SMELLS OF TROLLS. THERE ARE EXITS TO THE EAST AND WEST."
110 INPUT A$
120 IF LEFT$(A$, 1) = "W" OR RIGHT$(A$, 4) = "WEST" GOTO 200
125 IF LEFT$(A$, 1) = "E" OR RIGHT$(A$, 4) = "EAST" GOTO 300
130 PRINT "YOU CAN'T GO THERE FROM HERE."
140 GOTO 110

200 REM HALLWAY
210 PRINT "YOU ARE IN THE HALLWAY..."
220 END

300 REM CLASSROOM
310 PRINT "YOU ARE IN THE CLASSROOM..."
320 END
```


[BASIC Language Reference](https://www.apple.asimov.net/documentation/programming/basic/Applesoft%20BASIC%20Quick%20Reference%20Guide.pdf)


