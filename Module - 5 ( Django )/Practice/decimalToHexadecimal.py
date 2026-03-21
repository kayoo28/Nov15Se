num= int(input("Enter the number(Decimal) : "))

sum=""
key=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']

while(num!=0):
    rem=num%16
    sum=key[rem] + sum
    num=num//16

print(sum)