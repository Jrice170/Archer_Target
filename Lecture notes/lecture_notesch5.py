from math import *

a = "Hi"
b = "joe"
c = a+b

#print(b[0])
print(chr(ord("h")+1))  ### 7 puts in cription
##48 to 122
### key bord input no input statement
print(round(pi,3))
print("this is pi = {0:5f}".format(pi))

## note pade read file
## how to open a text file
#### takes out of file


infile=open("Textfile.txt","r")
instring=infile.read()
instring=infile.read()
##print(infine.read())
print(instring)
### put the file 
outfile=open("testfile.txt","w")
outfile.write("this ia an out file")
print("this is an outfile",file=outfile)
for ch = instring
    outfile.write(chr(ord(ch)+1))

##outfile.write("this agen")
outfile.close()


      

