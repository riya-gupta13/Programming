    # *
#    * *
#   *   *
#  *     *
# *       *
#  *     *
#   *   *
#    * *
#     *


n = 5
for i in range(0, n):
    for j in range(n - i):
        print(" ", end="")
    for j in range(i * 2 + 1):
        if j == 0 or j == (i * 2):
            print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(0, n):
    for j in range(i + 1):
        print(" ", end="")
    for j in range(2 * (n - i) - 1):
        if j == 0 or j == 2 * (n - i) - 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()
