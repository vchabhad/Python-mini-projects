from functions_of_python import count

str1= input("Enter string:")
count1,count2 = count(str1)

print("The number of lowercase characters is:")
print(count1)
print("The number of uppercase characters is:")
print(count2)