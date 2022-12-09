# * * * * *
#  * * * *
#   * * *
#    * *
#     *
#     *
#    * *
#   * * *
#  * * * *
# * * * * *

n = 5
for i in range(5, 0, -1):
    for k in range(n - i):
        print(" ", end="")
    for j in range(i):
        print("*", end=" ")
    print(" ")
for i in range(1, n + 1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(i):
        print("*", end=" ")
    for j in range(n-i):
        print(" ", end="")
    print(" ")
