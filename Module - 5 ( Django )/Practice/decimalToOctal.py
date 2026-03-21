num= int(input("Enter the number(Decimal) : "))

sum=0
m=1

while(num!=0):
    rem=num%8
    sum=sum+(rem*m)
    num=num//8
    m=m*10

print(sum)