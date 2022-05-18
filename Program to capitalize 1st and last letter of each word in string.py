#program to capitalize first and last letter of each word of string
#take input from user
str=input("Enter string:")
#convert first letter of each word to capital
str=str.title()
result=""
#convert last letter of each word to capital
str1=str.split()
for word in str1 :
    result +=word[:-1] + word[-1].upper() + " "
#print final output
print("Your output:", result)