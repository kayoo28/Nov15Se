num = int(input("Enter the number(Octal) : "))

power=0
result=0

while num!=0:
    rem=num%10
    result=result + (rem*pow(8,power))
    power=power+1
    num=num//10

print(result)