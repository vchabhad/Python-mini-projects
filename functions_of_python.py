#sum of numbers

def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total


def conv_to_int(list1):
    for i in range(len(list1)):
        list1[i] = int(list1[i])

#reverse string

def rev_str(str):  
    str1 = ""  
    for i in str:  
        str1 = i + str1  
    return str1
#count upper and lowercase

def count(str):
    count1=0
    count2=0
    for i in str:
        if(i.islower()):
                count1=count1+1
        elif(i.isupper()):
                count2=count2+1
    return count1,count2