#FACTORIAL
# def fact(n):
#     if(n==0 or n == 1):
#         return 1
#     else:
#         return n*fact(n-1)

# n=6
# print(f"Factorial of {n} : {fact(n)}")

#Fibonacci Series
x1=0
x2=1 
def fib(n):
    if(n!=0):
        global x1,x2
        x3=x2+x1
        print(x3,end=" ")
       
        x1=x2
        x2=x3
        fib(n-1)


n = int(input("Enter the number of terms : "))
   
print(x1,x2,end=" ")
fib(n-2)

