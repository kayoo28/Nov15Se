'''
Types of Conditional Statements
    1). If Statement
    ). if-else Statement
    3). elif Statement
    4). Nested if Statement

Looping Statement : 
    1). for
    2). while

Control Statement : 
    1). break
    2). Continue
    3). pass
'''

#if-else
# age=15
# if age>=18:
#     print("Eligible for voting")
# else:
#     print("Not eligible for voting")

#Nested if-else
# a=10
# b=20
# c=30

# if a>b:
#     if a>c:
#         print("a is greater")
#     else:
#         print("c is greater")
# else:
#     if b>c:
#         print("b is greater")
#     else:
#         print("c is greater")

#if-else ladder
# a=10
# b=20
# c=30

# if a>b and a>c:
#     print("a is greater")
# elif b>c and b>a:
#     print("b is greater")
# elif c>a and c>b:
#     print("c is greater")
# else:
#     print("Something went wrong")


#Exercise
# marks = int(input("Enter Marks : "))

# if marks>=91 and marks<=100:
#     print("Grade A")
# elif marks>=71 and marks<=90:
#     print("Grade B")
# elif marks>=51 and marks<=70:
#     print("Grade C")
# elif marks>=35 and marks<=50:
#     print("Grade D")
# elif marks>=0 and marks<=34:
#     print("Grade E")
# else:
#     print("Invalid marks")


#Switch Case
# choice=5

# match choice:
#     case 1:
#         print("Gujarati")
#     case 2:
#         print("Hindi")
#     case 3:
#         print("English")
#     case _:
#         print("Invalid Input")

#Exercise
# num1 = int(input("Enter num1 : "))
# num2 = int(input("Enter num2 : "))

# option = input("Enter your choice(+,-,/,*) : ")

# match option:
#     case '+':
#         print("Addition : ",(num1+num2))
#     case '-':
#         print("Subtraction : ",(num1-num2))
#     case '*':
#         print("Multiplication : ",(num1*num2))
#     case '/':
#         print("Divison : ",(num1/num2))
#     case _:
#         print("Invalid Option")
    
#for loop

# for i in range(10):
#     print(i,end=" ")

# print("\n")

# for i in range(3,10):
#     print(i,end=" ")

# i=10
# while i<20:
#     print(i,end=" ")
#     i+=1


#Execise
choice='y'
while choice!='n':
    num1 = int(input("Enter num1 : "))
    num2 = int(input("Enter num2 : "))

    option = input("Enter your choice(+,-,/,*) : ")

    match option:
        case '+':
            print("Addition : ",(num1+num2))
        case '-':
            print("Subtraction : ",(num1-num2))
        case '*':
            print("Multiplication : ",(num1*num2))
        case '/':
            print("Divison : ",(num1/num2))
        case _:
            print("Invalid Option")
    choice=input("Enter you choice : ")

