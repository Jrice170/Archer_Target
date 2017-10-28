## Joseph Rice CS177 9/22/2017
## This code will compute the x-intercept when you enter the y-intercept 


from graphics import *
import math
### the following will be me building the frame work for the code 
def main():
## seting up the GraphWin with dementions and seting coords, the coords are set  
    win = GraphWin("Circle", 600,600)
    win.setCoords(-10,-10,10,10)
    win.setBackground("white")
## seting up the circle for back ground where the magic will happen 
    circ = Circle(Point(0,0),5)
    circ.setWidth(5)
    circ.setOutline("blue")
    circ.draw(win)
## setting the sumit button for the user to click to move the code along 
    button = Rectangle(Point(-2,1),Point(2,-1))
    button.draw(win)
### box where the x coords will pop up during code run, then i set where it would be in coords  
    case = Rectangle(Point(3.4,-3), Point(-2,-2))
    case.move(-0.5,0)
    case.move(0,-0.5)
    case.setWidth(2)
    case.setOutline("black")
    case.draw(win)
    #### set the word to submit to signal 
    sudmit = Text(Point(-1/2,0),"submit")
    sudmit.draw(win)


    # We have an entry point Now how do i get it in to a line
    y_intecept = Text(Point(-1,2), "Enter Y intercept(<5)")
    y_intecept.draw(win)
### Entry point where the user can input a number value useing Entry Function::: i also set the text to 0.0 useing the setText() after the Entry() function  point 
    y_entry = Entry(Point(2,2),3)
    y_entry.move(1,0)
    y_entry.setText("0.0")
    y_entry.draw(win)
### interface for the user to click to move the code along 

    win.getMouse()
### Text for the coment for the y intercept 
    x_intercept = Text(Point(-.7,-2), "   x intercept(x,-x):")
    x_intercept.draw(win)
### x output is where the printed statement for the x intercepts will be.
    x_output = Text(Point(0,-3),"") # use a set Text
    x_output.move(-.5,0)
    x_output.draw(win)
####  this is for the corisponding x
    x_output2 = Text(Point(1.5,-3),"")
    x_output2.move(-.5,0)
    x_output2.draw(win)

#### this turns the inputed value for the y axis into a value that can calculate the function 
    y_value = float((y_entry.getText()))
    sqrt_x = round(math.sqrt(25 - y_value**2),2)
    nsqrt_x = round(-1*math.sqrt(25 - y_value**2),2)
## the user needs to click agein 

    win.getMouse()
##
    line = Line(Point(sqrt_x,y_value),Point(nsqrt_x,y_value))
    line.setFill('red')
    line.setWidth(5)
    line.draw(win)
## code here is the two end circles at the end of the lines that corispond to the x intehrcept.

    end_circle = Circle(Point(sqrt_x,y_value), .1)
    end_circle.setFill("green")
    end_circle.draw(win)
    end_circle2 = Circle(Point(nsqrt_x,y_value), .1)
    end_circle2.setFill("green")
    end_circle2.draw(win)
    end_circle.setOutline("green")
    end_circle.setWidth(5)
    end_circle2.setOutline("green")
    end_circle2.setWidth(5)
    
 # change the text twice this will setText to difernttimes in different interval  changeing the text   
    sudmit.setText("click!")
    win.getMouse()
    x_output.setText(sqrt_x)
    x_output2.setText(nsqrt_x)

    sudmit.setText("Turn Off")
    win.getMouse()
    win.close()
    


input("press enter")
##
##
main()
##
##string_1 = "ashwhouhuoahjoa"
##print(string_1[:7])
##
##





5



















































