## Joseph Rice 10/16/2017
## this code will convert an immage from a gif to gray scale
## 
## psudo code 
""" for each row in the image:
    for each column in the image:
    r,g,b = get pixel information for current row and column
    brightness = int(round(0.299r + 0.587g + 0.114b))
    set pixel to color_rgb(brightness, brightness, brightness)
    update the image # to see progress row by row

            """

from graphics import *
## must size this right
win = GraphWin("converstion" ,500,500)

### function to convert color 
def colorless_picture_converter():
## input the file given in model
    file_name_input = input("please input file name here: ")
    file_name_output = input("save file to: ")
    
    
    image2 = Image(Point(0,0),file_name_input)
    

    width = int(image2.getWidth())
    width_center = int(width /2)
    height = int(image2.getHeight())
    height_center = int(height/2)
    image = Image(Point(width_center,height_center),file_name_input)
    image_window = GraphWin("Colorless Converter",width,height)
    image.draw(image_window)

    row = 0

    column = 0
### this loop will iterat as long as the value of the height
    
    for row in range(height):
## second loop will iterate as long as the width
        for column in range(width):
            red_value, green_value, blue_value = image.getPixel(column,row)
            gray_set = int(round(0.299* red_value + 0.587 * green_value + 0.144*blue_value))
            image.setPixel(column, row, color_rgb(gray_set, gray_set, gray_set))
            image_window.update()

    image.save(file_name_output)
    image_window.close()
    
    
    
colorless_picture_converter()

    
    

