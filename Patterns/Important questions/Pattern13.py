
#     *
#    * *
#   *   *
#  *     *
# *********
n = 5
for i in range(n):
    for j in range(n - i):
        print(" ", end="")
    for j in range(i * 2 + 1):
        if i == n-1:
            print("*", end="")
        elif j == 0 or j == (i * 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()







