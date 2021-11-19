## Todo

for next class:
- show obstacles for section II
- desk shares

- cover screen recording

```py
position(owl, draw_owl)

def draw_owl(owl):
    step = step_cycle(2, owl['wing_speed'])
    if step == 0:
        triangle(0, 0, -owl['size']*4, -owl['size']/2, -owl['size']*4, owl['size']/2)
    else:
        triangle(0, 0, -owl['size']*4, -owl['size']*2, -owl['size']*4, owl['size']*2)
                                                    ```
