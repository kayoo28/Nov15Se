day = int(input("Enter the days : "))

num=1
add=0
for i in range(0,day):
    num=num*2
    add=add+num

print(f"Sum : {add}")