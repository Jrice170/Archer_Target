### Joseph Rice 10/2/2017
##
##### Plan for this code down below
##""" 1. Set the background up for the target
##    2. Get the circles asighned to spasific points trough mouse clicks
##    3. Get the sum of the scores computed on the graphic window
##
##                                            """ 
##
##
##
##


maxX=minY = 10
maxY=minX = -10

from graphics import *
""" THIS SETS THE GRAPH WIN UP """ 
from math import pi as PIE
from math import sqrt
win = GraphWin("Archer Target", 600,600)
win.setCoords(minX,minY,maxX,maxY)
win.setBackground("green")

## CODE FOR CIRCLES 
center = Point(0,0)
c_white = Circle(center,5)
c_white.setFill("white")
c_white.draw(win)

c_black = Circle(center,4)
c_black.setFill("purple")
c_black.draw(win)

cblue = Circle(center,3)
cblue.setFill("Blue")
cblue.draw(win)

c_red = Circle(center,2)
c_red.setFill("red")
c_red.draw(win)
 
c_yellow = Circle(center, 1)
c_yellow.setFill("yellow")
c_yellow.draw(win)

Total_score = Text(Point(0,-9),"NO RULES!!!!!!!!!!")

Total_score.draw(win)
message = Text(Point(0,6), "Click To Shot Arrow")
message.setStyle("bold")
message.draw(win)

## list for storage 
total_score = []

## TEST CODE 
Try_1 = win.getMouse()
end_of_arrow = Point(-2,4)
## function for the calulation of radius
def radus(x,y):
    r = sqrt(x**2 + y**2)
    return r 
## TEST FUNCTION CODE
##value = radus(3,4)    
##print(value)

### function for the logic gate.
def score(r):
    if r <=1:
        value = 9
    elif r <=2:
        value = 7 
    elif r <=3:
        
        value = 5
    elif r <=4:
        
        value = 3
    elif r <=5:
        
        value = 2
    else:
        
        value = 0
    return value

r = radus(Try_1.getX(),Try_1.getY())
value = score(r)
total_score.append(value)
message_New = str(value) + " Points!"
Total_score.setText(message_New)

## 
line = Circle(Point(Try_1.getX(),Try_1.getY()),0.1)
line.setFill("black")
line.draw(win)

Try_2 = win.getMouse()
r = radus(Try_2.getX(),Try_2.getY())
value = score(r)
total_score.append(value)
message_New2 = str(value) + " Points !"
Total_score.setText(message_New2)

cir = Circle(Point(Try_2.getX(),Try_2.getY()),0.1)
cir.setFill("black")
cir.draw(win)

Try_3 = win.getMouse()
r = radus(Try_3.getX(),Try_3.getY())
value = score(r)
total_score.append(value)
message_New3 = str(value) + ' Points !'
Total_score.setText(message_New3)

cir_3 = Circle(Point(Try_3.getX(),Try_2.getY()),0.1)
cir_3.setFill("black")
cir_3.draw(win)

Try_4 = win.getMouse()
r = radus(Try_4.getX(),Try_4.getY())
value = score(r)
total_score.append(value)
message_New4 = str(value) + ' Points !'
Total_score.setText(message_New4)

cir_4 = Circle(Point(Try_4.getX(),Try_4.getY()),0.1)
cir_4.setFill("black")
cir_4.draw(win)

Try_5 = win.getMouse()
r = radus(Try_5.getX(),Try_5.getY())
value = score(r)
total_score.append(value)
message_New5 = str(value) + " Points !"
Total_score.setText(message_New5)

cir_5 = Circle(Point(Try_5.getX(),Try_5.getY()),0.1)
cir_5.setFill("black")
cir_5.draw(win)

message.setText("click to see total")
win.getMouse()
addition = 0


for i in total_score:
    number_value = int(i)
    addition = number_value + addition

message.setText("Your final score is:{0:7}".format(addition))

win.getMouse()

win.close()

