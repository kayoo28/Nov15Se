lines=5
for i in range(lines):
    for j in range(i):
        print(" ",end="")

    for k in range(lines-i):
        print("*",end="")
    print()