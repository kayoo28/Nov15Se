try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    op = input("Enter operator (+, -, *, /): ")

    if op == "+":
        print("Result:", num1 + num2)

    elif op == "-":
        print("Result:", num1 - num2)

    elif op == "*":
        print("Result:", num1 * num2)

    elif op == "/":
        print("Result:", num1 / num2)   

    else:
        print("Invalid operator")

except ValueError:
    print("Invalid input!")

except ZeroDivisionError:
    print("Cannot divide by 0")

except Exception as e:
    print("Something went wrong:", e)