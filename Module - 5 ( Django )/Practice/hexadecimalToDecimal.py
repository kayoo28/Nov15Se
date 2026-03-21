num = input("Enter the number(Hexadecimal) : ")
numrev=num[::-1]

power=0
result=0

for i in numrev:
    if(numrev.isdigit()):
        result = result + (int(i)*(16**power))
        power=power+1
    else:
        result = result + ((ord(i)-ord('A')+10)*pow(16,power))
        power=power+1

print(result)



'''
key=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
p=0
sum=0
for i in num[::-1]:
sum= sum + (key.index(i)*pow(16,p))
p=p+1
'''