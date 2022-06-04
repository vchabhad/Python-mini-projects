#python program to create a lambda function that adds 25 to a given number passed in as an argument
#input from user
value=int(input("Enter number: "))
add = lambda value: value + 25
print(add(value))