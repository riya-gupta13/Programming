# *********
#  *     *
#   *   *
#    * *
#     *
n = 5
for i in range(n):
    for j in range(i):
        print(" ", end="")
    for j in range(2 * (n - i) - 1):
        if i == 0:
            print("*", end="")
        elif j == 0 or j == 2 * (n - i) - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print(" ")
