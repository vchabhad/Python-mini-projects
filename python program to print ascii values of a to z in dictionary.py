#Python program to print a-z with ascii values
dictofascii={}
for val in range(97,123):
    key=chr(val)
    dictofascii[key]=val

print("a to z with it's ascii values :\n", dictofascii)
