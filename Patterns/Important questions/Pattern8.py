#     *
#    ***
#   *****
#  *******
# *********
n = 6
for i in range(1, n):
    temp = i
    for j in range(1, n - i):
        print(" ", end="")
    for k in range(0, (2 * i) - 1):
        print("*", end="")
    for m in range(1, n - i):
        print(" ", end="")
    print(" ")
