from graphics import *
win = GraphWin()
win.setBackground('orange')
for i in range(100):
    a = win.getMouse()
    a.draw(win)
    b = win.getMouse()
    b.draw(win)
    c = win.getMouse()
    c.draw(win)
    triangle = Polygon(a,b,c)
    triangle.setFill("red")
    triangle.setOutline("purple")

    triangle.draw(win)

    d = win.getMouse()
    d.draw(win)
    e = win.getMouse()
    e.draw(win)
    f = win.getMouse()
    f.draw(win)

    triangle_2 = Polygon(d,e,f)
    triangle_2.setFill("purple")
    triangle_2.setOutline("red")
    triangle_2.draw(win)

    center = win.getMouse()
    center.draw(win)
    circle = Circle(center, 30)
    circle.setFill("Blue")
    circle.setOutline("purple")
    circle.draw(win)


    
    

    
    
