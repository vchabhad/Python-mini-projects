# Python program to sort a list of tuples
 
list1 =[(2, 5), (1, 2), (4,4), (2, 3),(2,1)]
print("Before sorting :\n " + str(list1))

Llength = len(list1); 
for i in range(0, Llength):
    for j in range(0, Llength - i - 1):
        if(list1[j][-1] > list1[j + 1][-1]):
            swap = list1[j]
            list1[j] = list1[j + 1]
            list1[j + 1] = swap
 
print("After sorting : " + str(list1))