num = int(input("Enter the number : "))
x=num

power = len(str(num))
result=0

while num!=0:
    rem=num%10
    result=result + pow(rem,power)
    num=num//10

if result==x:
    print(f"{x} is armstrong number")
else:
    print(f"{x} is not armstrong number")
