n = int(input("Enter the number: "))

# Upper part
for i in range(1, n+1):
    for k in range(n, i-1, -1):
        print(" ", end="")
    for j in range(1, i+1):
        print(" *", end="")
    print()

# Lower part
for i in range(1, n+1):
    for k in range(1, i+1):
        print(" ", end="")
    for j in range(n, i-1, -1):
        print(" *", end="")
    print()


'''
lines=5
star=1
space=lines-1
mid=(lines//2)

for i in range()      
'''