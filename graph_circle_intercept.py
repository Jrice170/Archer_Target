

from graphics import *
import math
def main():
## seting up the GraphWin with dementions and seting coords 
    win = GraphWin("Circle", 600,600)
    win.setCoords(-10,-10,10,10)
    win.setBackground("white")
## seting up the circle for back ground
    circ = Circle(Point(0,0),5)
    circ.setWidth(5)
    circ.setOutline("blue")
    circ.draw(win)

    button = Rectangle(Point(-2,1),Point(2,-1))
    button.draw(win)

    case = Rectangle(Point(3.4,-3), Point(-2,-2))
    case.move(-0.5,0)
    case.move(0,-0.5)
    case.setWidth(2)
    case.setOutline("black")
    case.draw(win)
    Text(Point(-1/2,0),"submit").draw(win)


    # We have an entry point Now how do i get it in to a line
    y_intecept = Text(Point(-1,2), "Enter Y intercept(<5)")
    y_intecept.draw(win)
    y_entry = Entry(Point(2,2),3)
    y_entry.move(1,0)
    y_entry.setText("0.0")
    y_entry.draw(win)


    win.getMouse()

    x_intercept = Text(Point(-.7,-2), "   x intercept(x,-x):")
    x_intercept.draw(win)

    x_output = Text(Point(0,-3),"") # use a set Text
    x_output.move(-.5,0)
    x_output.draw(win)

    x_output2 = Text(Point(1.5,-3),"")
    x_output2.move(-.5,0)
    x_output2.draw(win)

    

    y_value = eval(y_entry.getText())
    sqrt_x = round(math.sqrt(25 - y_value**2),2)
    nsqrt_x = round(-1*math.sqrt(25 - y_value**2),2)

    win.getMouse()
##
    line = Line(Point(sqrt_x,y_value),Point(nsqrt_x,y_value))
    line.setFill('red')
    line.setWidth(5)
    line.draw(win)
##

    end_circle = Circle(Point(sqrt_x,y_value), .1)
    end_circle.setFill("purple")
    end_circle.draw(win)
    end_circle2 = Circle(Point(nsqrt_x,y_value), .1)
    end_circle2.setFill("green")
    end_circle2.draw(win)
    end_circle.setOutline("green")
    end_circle.setWidth(5)
    end_circle2.setOutline("green")
    end_circle2.setWidth(5)
    
    
    
    win.getMouse()
    x_output.setText(sqrt_x)
    x_output2.setText(nsqrt_x)


input("press enter")


main()

string_1 = "ashwhouhuoahjoa"
print(string_1[:7])







5



















































