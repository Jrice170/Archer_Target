

##defining functions 
##def main():
##   print("Happy birthday to you!")
##   print("Happy birthday, dear Fred.")
##   print("Heppy birthday to you!")
##
##main()
##
##
##def happy():
##    print("Happy birthday to you!")
##    
##happy()


##def happy():
##    print("Happy Birthday to you!")
##
##def sing(person):
##    happy()
##    happy()
##    print("Happy birthday, dear", person + ".")
##    happy()
##
##def main():
##    
##    sing("Fred")
##    print()
##    
##    sing("Lucy")
##    print()
##    
##    sing("Elmer")
##
##main()

##from graphics import * 
##
##def drawBar(window, year, height):
##    # dra a bar in window starting at year with given height
##    bar = Rectangle(Point(year,0), Point(year+1,height))
##    bar.setFill("green")
##    bar.setWidth(5)
##    bar.draw(window)
##
##def main():
##    #introduction
##    print("This program plots the growth of a 10-year investment.")
##
##
##    # Get principal and interest rate
##    principal = eval(input("Enter the inital principal: "))
##    apr = eval(input("Enter the annualized interest rate: "))
##    ## Create a graphics window with labels on the left edge
##    win = GraphWin("Investment Growth Chart",320,240)
##    win.setBackground("white")
##    win.setCoords(-1.75,-200,11.5,10400)
##    Text(Point(-1,0),"0.0K").draw(win)
##    Text(Point(-1,2500),"2.5K").draw(win)
##    Text(Point(-1,5000),"5.0K").draw(win)
##    Text(Point(-1,7500),"7.5K").draw(win)
##    Text(Point(-1,10000),"10.0K").draw(win)
##
##    draw(win, 0, principal)
##    for year in range(1,11):
##        principal = principal * (1 + apr)
##        drawBar(win, year, principal)
##    win.close()
##
##main()
####
####import math
####from graphics import *
####
####def square(x):
####    return x * x
####
####def distance(p1,p2):
####    dist = math.sqrt(square(p2.getX() - p1.getX())
####                     + square(p2.getY() - p1.getY()))
####    return dist
####def main():
####    win = GraphWin("Draw a Triangle")
####    win.setCoords(0.0,0.0,10.0,10.0)
####    message = Text(Point(5, 0.5), "Click on three point")
####
####
####    ## get and draw three vertices of triangle
####    p1 = win.getMouse()
####    p1.draw(win)
####    p2 = win.getMouse()
####    p2.draw(win)
####    p3 = win.getMouse()
####    p3.draw(win)
####
####    triangle = Polygon(p1,p2,p3)
####    triangle.setFill("peachpuff")
####    triangle.setOutline("cyan")
####    triangle.draw(win)
####
####    perim = distance(p1,p2) + distance(p2,p3) + distance(p3,p1)
####    message.setText("The perimeter is: {0:2.0f}".format(perim))
####
####    # what for mouse click
####
####    win.getMouse()
####    win.close()
####
####main()


## addinterest rate
def addInterest(balance, rate):
    newBalance = balance * (1+rate)
    balance = newBalance 

def test():
    amount = 1000
    rate = 0.05
    addInterest(amount,rate)
    print(amount)










































    
















































