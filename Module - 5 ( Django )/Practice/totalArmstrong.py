for i in range(100,1000):
    result=0
    temp=i

    while i!=0:
        rem=i%10
        result=result + pow(rem,3)
        i=i//10
    
    if temp==result:
        print(temp,end=" ")
