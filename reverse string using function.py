#reverse a string using function

def rev_str(str):  
    str1 = ""  
    for i in str:  
        str1 = i + str1  
    return str1

#take input from user
input_str= input("Enter string to reverse:")

rev_str1= rev_str(input_str)

print("Reversed string :", rev_str1)