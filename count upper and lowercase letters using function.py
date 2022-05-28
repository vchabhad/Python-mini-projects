
def count(str):
    count1=0
    count2=0
    for i in str:
        if(i.islower()):
                count1=count1+1
        elif(i.isupper()):
                count2=count2+1
    return count1,count2

str1= input("Enter string:")
count1,count2 = count(str1)

print("The number of lowercase characters is:")
print(count1)
print("The number of uppercase characters is:")
print(count2)