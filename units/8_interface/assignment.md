## Sketch #8: Interface

For this sketch, you will create a software painting interface using code. To get started, think about programs like [MacPaint](https://en.wikipedia.org/wiki/MacPaint), where the "user" can choose from multiple brushes with the mouse and use them to draw on the open canvas. However, your approach should reflect an artistic purpose for your own use or for someone else. For example, imagine the difference between interfaces for artists with a [street-art aesthetic](https://www.google.com/search?q=graffiti&tbm=isch) using spray-paint brushes, or a [futurist](https://www.google.com/search?q=future+interface&tbm=isch) interface, or maybe one for someone who is [color blind](https://en.wikipedia.org/wiki/Color_blindness), or a [bird](https://en.wikipedia.org/wiki/Bird_vision#Light_perception), or [underwater](http://thedivingblog.com/colors-underwater/).

Along with your code and [3-sentence description](../../resources/description_guidelines.md), you should supply an image that you have created to demonstrate the capabilities of your interface. Your interface must include at least four different "brushes" or ways of interacting. A rough version should be complete for the last day of class—this will be our crit, where you will swap interfaces with each other. Your final version is due the last day of exam week (you are welcome and encouraged to turn it in sooner).



### Example from class

```py

def setup():
    global brush
    size(500, 500)
    background(255)    
    brush = "brush_1"
    
def draw():
    global brush
            
    if mousePressed == True:
        noCursor()    
    
        if brush == "brush_1":
            stroke(0)
            delta = dist(pmouseX, pmouseY, mouseX, mouseY)
            strokeWeight(delta) 
            stroke(255, 0, swing(0, 255, 50))           
            point(mouseX, mouseY)

        elif brush == "brush_2":            
            strokeWeight(1)
            stroke(0, 255, 0, 50)
            line(mouseX - 20, mouseY - 20, mouseX + 20, mouseY + 20)
    
    else:        
        cursor()
            
            
    # draw the buttons
    noStroke()
    fill(250)
    rect(0, 0, 50, height)
    
    if brush == "brush_1":
        strokeWeight(5)
        stroke(0)
    else:
        noStroke()
    fill(255, 0, 0)
    square(10, 10, 30) 

    if brush == "brush_2":
        strokeWeight(5)
        stroke(0)
    else:
        noStroke()    
    fill(0, 255, 0)
    square(10, 50, 30)
            
    
    
def mouseReleased():    
    global brush
    
    if mouseX > 10 and mouseX < 40 and mouseY > 10 and mouseY < 40:
        print("The red button was clicked")
        brush = "brush_1"
        
    if mouseX > 10 and mouseX < 40 and mouseY > 50 and mouseY < 80:
        print("The green button was clicked")
        brush = "brush_2"
      
      
      
def change(start, stop, duration, offset=0):
    if duration == 0:
        duration = 1    
    return map((frameCount + offset) % duration, 0, duration, start, stop)


def swing(start, stop, duration, offset=0): 
    # duration is one half of the swing
    position = -cos(2 * PI * change(0, 1, duration * 2, offset)) * .5 + .5
    return (position * (stop - start)) + start    
```

Additional code tutorial [here](code.md)