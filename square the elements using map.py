# Python program to square the elements of the list using map function

def square(n):
  return n * n
lst1 = [4, 5, 2, 9]
print("Original List: ",lst1)
result = map(square, lst1)
print(list(result))
