# * 
# ** 
# *** 
# **** 
# *****

lines=int(input("Enter the number of lines : "))

for i in range(lines):
    for j in range(i+1):
        print("*",end="")
    print()