x=0
y=1

length = int(input(" Enter the length : "))

print(x,y,end=" ")
for i in range(length-1):
    z=x+y
    x=y
    y=z
    print(z,end=" ")
