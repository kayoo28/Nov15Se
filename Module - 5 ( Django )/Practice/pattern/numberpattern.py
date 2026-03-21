n=int(input("Enter the number: "))


# 1
# 23
# 456
# 78910
# count=1
# for i in range(lines):
#     for j in range(i):
#         print(count,end="")
#         count=count+1
#     print()

# 1
# 12
# 123
# 1234
# 12345
# for i in range(n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()

# 5
# 45
# 345
# 2345
# 1234
# for i in range(n,0,-1):
#     for j in range(i,n+1):
#         print(j,end="")
#     print()


# 0
# 10
# 010
# 1010
# 01010

for i in range(n):
    for j in range(i+1):
            print((i-j)%2,end="")
    print()