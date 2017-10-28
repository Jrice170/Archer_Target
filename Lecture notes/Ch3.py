import math ## import math library so I can use square root function
num = eval(input("enter the number"))
irt = eval(input("enter the number of iterations"))
gs = num/2
print("      Guess   ","     Answer     ","    % Error  ")
for i in range(irt):
    gs=(ga + (num/gs))/2
    er=abs((gs-math.sqrt(num)/(math.sqrt(num))*100
    print(gs ,  math.sqrt(num) , er)
            
    

