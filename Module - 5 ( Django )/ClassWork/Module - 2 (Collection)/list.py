# l = [100,200,300,400,200,"abc",True,45.66]
# print(l)
# print(len(l))
# print(type(l))

l = list((1,2,3,4,5,6,7,8,9))
print(l)
print(len(l))
print(type(l))

print(l[0])
print(l[-1])
print(l[2:])
print(l[2:5])
print(l[-4:-1])
print(l[1:8:2])
print(l[::-1])


#append
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)

#Clear
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
print(fruits)

#Copy
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)

#Count
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
print(x)

#Extends
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)

#Index
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)

#Insert
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)

#Pop
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)

#Removes
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)

#Reverse
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)

#Sort
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)

cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars)

a = ["b", "g", "a", "d", "f", "c", "h", "e"]
x = sorted(a)
print(x)

'''
append()
clear()
copy()
count()
extend()
index()
insert()
pop()
remove()
reverse()
sort()
sorted()
del
'''