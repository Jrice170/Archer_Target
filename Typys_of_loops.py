""" typys_of_loops.py"""

## for loops

""" indifinate loop """
##i = 0
##while i <=10:
##    print(i)
##    i = i + i ## it would be indefinate 
#### this code is the same thing
##    for i in range(11):
##        print(i)
##
##def main():
##    sum = 0.0
##    count = 0
##    moredata = "yes"
##
##    white moredata[0] == "y"
##    x = eval(input("enter a number >> "))
##    sum = sum + x
##    count = count + 1
##    moredata = input("Do you have more numbers (yes or no ?) ")
##print("\n The average of the numbers is", sum /count)


## here is a general pattern for desinging a sentinel loop
"""get the first data item
    while item us not the sentinel
        process the item
        get the next data item"""

## interactive loop
def main():
    sum = 0.0
    count = 0
    x = eval(input("enter a number (negative to quit)>> "))
    while x >= 0:
        sum = sum +x
        count = count + 1
        x = eval(input("Enter a number (negative to quit) >> "))
    print("\nThe average of the numbers is", sum/count)

main()

#### string converter
##def main():
##    sum = 0.0
##    count = 0
##    xStr = input("enter a number (<Enter> to quit)>>")
##print("\nThe average of the numbers is", sum/count)


def main():
    sum = 0.0
    count = 0
    xStr = input("enter a number (Enter to quit)) ")
    while != "":
        x = eval(xStr)
        sum =+ x
        count =+ 1
        xStr = input("enter a number (enter to quit )>> ")
    print("\nThe average is: ", sum/count)

#### This is important to know how to reade from a file.
##def g():
##    fileName = input("What file are the numbers in? ")
##    infile = open(fileName,"r")
##    sum = 0.0
##    count = 0
##    for line in infile:
##        sum = sum + eval(line)
##        count = count + 1
##    print("\nThe average of the numbers is",sum / count)

##### for the while loop## this will be useful for looping through list. 
##def v():
##    fileName = input("what file are the numbers in? ")
##    infile = open(fileName,"r")
##    sum = 0.0
##    count = 0
##    line = infile.readline()
##    while =! "":
##        sum = sum + eval(line)
##        count = count + 1
##        line = infile.readline()
##    print("\nThe average of the numbers is",sum / count)
##
##def infortant():
##    fileName = input("what file are the numbers in?")
##    infile = open(fileName,"r")
##    sum = 0.0
##    count = 0
##    line = infile.readline()
##    while line != " ":
##        for xStr in line.split(",")
##        sum = sum + eval(xStr)
##        count = count + 1
##    line = infile.readline()
##print("\nThe average of the numbers is", sum/count)
##
##
##
##
##def main():
##
##    filename = input("what is the file name: ")
##    infile = open(filename,"r")
##    sum = 0.0
##    count = 0
##    line = infile.readline()
##
##    while line !="":
##
##        sum = sum + eval(line)
##        count = count + 1
##    line = infile.readline()
##
##print("\nThe average of the numbers is", sum/count)
##
##    

def main():
    
    data = input("enter a number (hit enter to quit) ") 

    sum = 0
    count = 0 

    while sum not => 15 or count => 20:
        
        sum = sum + data
        count = count + 1

    data = input('enter a number (hit enter to quit)')


        






        





















    
