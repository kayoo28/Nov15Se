
#Creating Tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple)

#Acessing Tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
print(thistuple[-1])

#Slicing Tuples
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#Updating Tuples
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

'''
count()
index()
'''