## Todo

examples for assignment page (and later lecture):
- one time trigger
- season timer (with dice rolling)
- age timer
- spawn (maybe not)

for next class:
- show the weird draw thing
    - first draw it pointy
    - separate out a function to draw it
    - then use the position function
- step_cycle animation
- show obstacles




```py
position(owl, draw_owl)

def draw_owl(owl):
    step = step_cycle(2, owl['wing_speed'])
    if step == 0:
        triangle(0, 0, -owl['size']*4, -owl['size']/2, -owl['size']*4, owl['size']/2)
    else:
        triangle(0, 0, -owl['size']*4, -owl['size']*2, -owl['size']*4, owl['size']*2)
                                                    ```



----

- cut interface
- have emergence crit the Monday before thanksgiving, have the wednesday be an extended office hours "work" day to talk about final project
- final project proposals due after thanksgiving
