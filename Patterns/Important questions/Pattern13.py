#     *
#    * *
#   *   *
#  *     *
# *********
n = 6
for i in range(1, n):
    for j in range(0, n - i):
        print("#", end="")
        if i+j==n:
            for k in range(i):
                print("*",end="")
    for m in range(0, n - i):
        print("#", end="")
    print(" ")
