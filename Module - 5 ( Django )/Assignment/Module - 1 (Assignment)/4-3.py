per = float(input("Enter the percentage : "))

if per>=90:
    print("Grade A")
elif per>=75 and per<90:
    print("Grade B")
elif per>=60 and per<75:
    print("Grade C")
elif per>=45 and per<60:
    print("Grade D")
elif per>=33 and per<45:
    print("Grade E")
else:
    print("Grade F")