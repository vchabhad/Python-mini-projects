#program to check special characters in string
#Get input from users
str=input("Enter string: ")
flag = 0
special="!@#$%^&*()-+?_=,<>/"

for i in str :
    for j in special:
        if i==j :
            flag = 1
            
if flag == 0:
    print("string accepted")
else:
    print ("string not accepted")