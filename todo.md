## Todo

next class:
- have them re-download the sim_helpers (first class never did)
- paste in the example

then:
- show time from lecture notes
- show the weird draw thing
    - first draw it pointy
    - separate out a function to draw it
    - then use the position function

- step_cycle



```py
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
