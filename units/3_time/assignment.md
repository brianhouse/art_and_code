## Sketch #6: Time

Create a sketch with some aspect of time as its central theme. Draw upon techniques from past units and combine them with Processing's events to express your idea.

Your code should include your title and a [3-sentence statement](../../resources/statement_guidelines.md) that conveys your concept. In addition, turn in a screen recording of your animation. Just record the processing window; we shouldn't see any extraneous windows.


### Information for making screen recordings
- [MacOS](https://support.apple.com/guide/mac-help/take-a-screenshot-or-screen-recording-mh26782/mac)
- [Windows](https://betanews.com/2020/01/20/windows-10-screen-record-xbox-game-bar/)



### Time Functions

```py
def change(start, stop, duration, offset=0):
    return map((frameCount - offset) % max(duration, 1), 0, duration, start, stop)

def swing(start, stop, duration, offset=0): 
    position = -cos(2 * PI * change(0, 1, duration * 2, offset)) * .5 + .5
    return (position * (stop - start)) + start  
```


### Examples

<p>
  <img src="examples/caroline_wu_curtained_sunrise.gif" width="400" /><br />
  Caroline Wu, <i>Curtained Sunrise</i> (2023)<br />
</p>

<p>
  <img src="examples/hypnotic_weave_daniel_dachille.gif" width="400" /><br />
  Daniel Dachille, <i>Hypnotic Weave</i> (2023)<br />
</p>