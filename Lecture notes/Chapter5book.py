str1 = "Hello"
str2 = "spam"

print(str1,str2)
type(str1)
type(str2)


print(len("spam"))
greet = "Hello Bob"
print(greet[0])
print(greet[:])
print(greet[:4])
print(greet[:5])
print(greet[1:6])
print(greet[2:4])
print(greet[-1])

message = "spam" + "c" + "m"
print(message)
you = "you"
can = "can"
add = "add"
strings = "strings"
print(you, can, add, strings, "like that")

##len_c = len("nnnnnnnnnnnnnnnnnnnn")
##print(len_c)

def main():
    print("this program generates usernames.")

    
    first = input("Please enter your first name (all lowercase): ")
    last = input("what is your last name(all lowercase): " )
    user_name = last[0] + first[:6]
    print("your user name will be" ,user_name)
    
main()



    



 

