# * * * *
# *     *
# *     *
# * * * *


n = 4
for i in range(1, n + 1):
    if i == 1 or i == n:
        for j in range(n):
            print("*", end="")
    else:
        for j in range(1):
            print("*", end="")
        for j in range(n - 2):
            print(" ", end="")
        for j in range(1):
            print("*", end="")
    print(" ")
