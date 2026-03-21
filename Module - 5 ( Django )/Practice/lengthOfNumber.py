num = int(input("Enter the number : "))
temp=num

count = 0
while num!=0:
    num=num//10
    count=count+1
print(f"Length of  {temp} : {count}")
