num = int(input("Enter the number : "))
x=num
fact = 1

while num!=0:
    fact=fact*num
    num=num-1

print(f"Factorial of {x} : {fact}")