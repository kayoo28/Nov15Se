try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    result = a / b
    print("Result:", result)

    my_list = [10, 20, 30]
    index = int(input("Enter index (0-2): "))
    print("Value:", my_list[index])

except ValueError:
    print("Invalid input!")

except ZeroDivisionError:
    print("Cannot divide by 0")

except IndexError:
    print("List index out of range ❌")

except Exception as e:
    print("Sonething went wrong:", e)

finally:
    print("Program finished 👍")