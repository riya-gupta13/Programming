#    *
#   ***
#  *****
# *******
# *********
# *********
# *******
#  *****
#   ***
#    *
n = 5
for i in range(1, n+1):
    for j in range(1, n - i):
        print(" ", end="")
    for k in range(0, (2 * i) - 1):
        print("*", end="")
    for m in range(1, n - i):
        print(" ", end="")
    print(" ")
for i in range(n, -1, -1):
    for j in range(1, n - i):
        print(" ", end="")
    for k in range(1, (2 * i)):
        print("*", end="")
    for m in range(1, n - i):
        print(" ", end="")
    print(" ")
