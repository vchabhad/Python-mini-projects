from functions_of_python import sum,conv_to_int

input1= input('Enter elements of a list separated by space : ')
print("\n")
list1 = input1.split()

conv_to_int(list1)
sum = sum(list1)


print("sum of entered numbers of list :", sum)