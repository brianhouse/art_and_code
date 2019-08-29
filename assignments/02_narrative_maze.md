# Sketch #2: Narrative Maze

Using BASIC, create an interactive story (such as Zork) where the reader/interactor moves from one "room" to another using keyboard commands. For full credit, your program must demonstrate at least 5 different "rooms"; you may also want to have objects that can be carried between rooms and which have an affect on the narrative. 

Key statements:
`PRINT "HELLO WORLD`
`INPUT A$`
`IF ... GOTO`

Commands to compare strings:
`LEFT$`
`RIGHT$`
`MID$`

Other fun statements:
`INVERSE`
`NORMAL`
`FLASH`


One challenge working with BASIC is organizing your line numbers. You may want to reserve 100 line numbers for every state. 

For example:
```
100 PRINT "YOU ARE IN FIELDS 205. IT IS A DARK ROOM THAT SMELLS OF TROLLS. THERE ARE EXITS TO THE NORTH AND WEST."
110 INPUT A$
120 IF LEFT$(A$, 2) = "GO" AND MID$(A$, 4, 1) = "N" GOTO 200
125 IF LEFT$(A$, 2) = "GO" AND MID$(A$, 4, 1) = "W" GOTO 300
130 PRINT "YOU CAN'T DO THAT HERE."
140 GOTO 110

200 PRINT "YOU ARE IN THE HALLWAY..."

300 PRINT "YOU ARE IN THE CLASSROOM..."
```


[Reference](https://www.apple.asimov.net/documentation/programming/basic/)Applesoft%20BASIC%20Quick%20Reference%20Guide.pdf


