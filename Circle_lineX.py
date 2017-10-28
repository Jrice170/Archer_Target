## Joseph Rice 9/11/2017 
## This program Will have a Circle with a line intersector
## Blue print down below then code

### inputs: Center Circle A point(0,0) randius of 5 units
### inputs: set up coords form -10,-10 to 10,10
### inputs: line going across window
### inputs: second line goes from one side and other like an x
### both lines are red .setaFill
## import form the graphics

from graphics import *
## Setting the stage 
win = GraphWin("Circle", 600, 600)
## Set coords for graphics window 
win.setCoords(-10, -10, 10, 10)
## def center in the mid of graphic 
center = Point(0,0)
## def center in circle 
circ = Circle(center, 5)
circ.setFill("darkorange")
circ.draw(win)
## line that will intersect midel
line = Line(Point(-10,-10), Point(10,10))
line.setFill("red")
line.draw(win)
## second line will intersect a center of circle
line2 = Line(Point(10,-10), Point(-10,10))
line2.draw(win)
line2.setFill("red")
## this is the left eye 
Left_eye = Circle(Point(5,5), 1)
Left_eye.setFill("green")
Left_eye.draw(win)
Left_eye.move(-3,-3)
## Right Eye
Right_eye = Left_eye.clone()
Right_eye.move(-4,0)
Right_eye.setFill("green")
Right_eye.draw(win)

##mouth = Oval(Point(2,-6), Point(5,5))
mouth = Oval(Point(-3.5,-4), Point(2,-6))
mouth.move(0,2)
mouth.move(1,0)
mouth.setFill("yellow")
mouth.setOutline("Purple")
## Puple 
c = Circle(Point(2,5), .5)
c.move(0,-3)
c.setFill("red")
c.draw(win)
## Puple 
c2 = c.clone()
c2.move(-4,0)
c2.setFill('red')
c2.draw(win)
### rectangular hat 
hat = Rectangle(Point(-3,1), Point(1,5))

hat.move(0,3)
hat.move(1,0)
hat.setFill("pink")
hat.draw(win)

mouth.draw(win)
### text for the face
Text(Point(6,7), "It's a face").draw(win)
Text(Point(-5,1), "Green Eyes").draw(win)

input("Press enter")
print("Click the face !!!")

for i in range(2):
    p = win.getMouse()
    text = Text(Point(5,-4), "Hello !")
    text.setFill("blue")
    text.draw(win)
    print("Its alive !!!!!!!!!!!!!!!!!!!!!")
    
    
input("Press <Enter> to quit")

win.close()









