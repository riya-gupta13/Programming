# *********
#  *******
#   *****
#    ***
#     *

n = 5
for i in range(n, -1, -1):
    for j in range(0, n - i):
        print(" ", end="")
    for k in range(0, (2 * i) - 1):
        print("*", end="")
    for m in range(0, n - i):
        print(" ", end="")
    print("")
