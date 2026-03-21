n = int(input("Enter the number: "))

# Upper part
for i in range(1, n+1):
    for k in range(n, i-1, -1):
        print(" ", end="")
    for j in range(1, i+1):
        if j == 1 or j == i:
            print(" *", end="")
        else:
            print("  ", end="")
    print()

# Lower part
for i in range(1, n+1):
    for k in range(1, i+1):
        print(" ", end="")
    for j in range(n, i-1, -1):
        if j == n or j == i:
            print(" *", end="")
        else:
            print("  ", end="")
    print()