#Python program to square the elements of the list using lambda and map function

lst1= [4, 5, 2, 9]
result = map(lambda v: v*v,lst1)
print(list(result))
