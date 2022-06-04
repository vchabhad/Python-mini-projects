#triple all numbers using map
def triple(n):
  return n * 3
lst1 = [1,2,3,4,5,6,7]
print("Original List: ",lst1)
result = map(triple, lst1)
print(list(result))