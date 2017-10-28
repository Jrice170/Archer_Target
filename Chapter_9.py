## Joseph Rice 10/13/2017


"""This code it going to randamly generate dots on to a graphics window.
The code below will do a calulation for random dots.
This code will allso show the calculation for the percentage that hit the circle.

first import the random modual 'from random import *'
next import the graphics modual. 'from graphics import *
import math 
1. input the number of dots generated
2. outputs generate the graphic picture of what is happening
"""

from random import *
import math 
from graphics import * 

## function for the whole background the the graphical picture

def whole():
    win = GraphWin("Pi Simulation",600,600)
    win.setBackground("purple")
    center = Point(0,0)

# function for the Corrds

    def plan(win):


        return win.setCoords(2.5,-2.5,-2.5,2.5)

## ## function for the rectange
    def rectangle(win):
        
        rect = Rectangle(Point(-1,-1),Point(1,1))
        rect.setOutline("black")
        rect.setFill("red")
        rect.setWidth(1)
        return rect.draw(win)
    ## this draws the simulated circle 
    def circle(win):
        cir = Circle(center,1)
        cir.setOutline("red")
        cir.setWidth(3)
        cir.setFill("black")
        
        return cir.draw(win)

    ### draws each individual point 
 ### this function draws all of the objects 
    def draw_background():
        plan(win)
        rectangle(win)
        circle(win)
        
    draw_background()

  
    def main():

##        number_dots = eval(input("enter the number of dots: "))
##        n = 1 ## range stops before the number you put in>>>
##        Total_darts = n + number_dots
##        hits = 0
### TAKE NOTE** I ADDED A WHILE LOOP TO MAKE MY PROGRAM MORE USER FREANDLY
##      WHTA THE WHILE LOOP DOES:: WILL CONDINUE RUNING AS LONG AS THE USER DOES NOT ENTER A LETTER
        state = input("Press enter to continue <enter>")
## while state does not have a string in it will condinue runing 
        while state == "":
##            state = input("Press enter to coninue: <enter> or typy a letter to stop")
            number_dots = eval(input("enter the number of dots: "))
            n = 1 ## range stops before the number you put in>>>
            Total_darts = n + number_dots
            hits = 0
## I WITH OUT THE IF STATEMENT THE LOOP WHOULD BE INFINITE. 
            if state != "":
                break
            state = input("Press enter to show dots on display: typy, NO to stop")
#### This for loop WILL LOOP HOW MANY TIMES THE USER INPUTS FOR TOTAL_DARTS
            for i in range(0,Total_darts):
        ####
                x = random()*2 - 1
        ####
                y = random()*2 - 1
        ##
                p = Point(x,y)
                blue = "blue"
                p.draw(win)
                p.setFill(blue)

        ##4
                in_circle = x**2 + y**2
                
                if in_circle <= 1:
                    hits += 1
                   
  ##          calculations
            pi = 4*(hits/Total_darts)
            ave = hits/Total_darts
            print("Percent That hit the circle ", float(round(ave*100,2)),"%")
            print("The average of pi" + "~", round(pi,3))
    

        
    main()
        
            
whole()



    

        
        
        
        
    




