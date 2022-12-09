#     *
#    * *
#   * * *
#  * * * *
# * * * * *
n = 6
for i in range(1, n):
    for j in range(n - i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    for j in range(n - i):
        print(" ", end="")
    print(" ")
