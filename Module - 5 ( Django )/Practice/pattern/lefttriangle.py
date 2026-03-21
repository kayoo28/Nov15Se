lines=5
for i in range(lines):
    for j in range(lines-i-1):
        print(" ",end="")

    for k in range(i+1):
        print("*",end="")
    print()