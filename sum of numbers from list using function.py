def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total

# convert each item to int type
def conv_to_int(list1):
    for i in range(len(list1)):
        # convert each item to int type
        list1[i] = int(list1[i])



input1= input('Enter elements of a list separated by space : ')
print("\n")
list1 = input1.split()

conv_to_int(list1)
sum = sum(list1)


print("sum of entered numbers of list :", sum)