#take input from user
from ssl import ALERT_DESCRIPTION_UNEXPECTED_MESSAGE


str1=input("Enter string")
#for caseless comparison
str1=str1.casefold()
vowels="aeiou"
count=0
for i in str1:
    for x in vowels :
        if i==x :
            count= count + 1

print(count) 