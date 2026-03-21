num = int(input("Enter the number : "))
temp=num
result=0

while num!=0:
    rem=num%10
    num=num//10
    result= result*10 + rem


if(temp==result):
    print(f"{temp} is palindrome")
else:
    print(f"{temp} is not palindrome")