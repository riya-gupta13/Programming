# 1            1                 [1, 6 , 1]
# 1 2        2 1                 [2,4,2]
# 1 2 3    3 2 1                 [3,2,3]
# 1 2 3 44 3 2 1                 [4,0,4]


n = 5
space = 2 * (n - 1)

for i in range(1, n):  # no of rows
    # numbers
    for j in range(1, i + 1):
        print(j, end="")
    # space
    for k in range(1, space):
        print(" ", end="")
    # numbers
    for j in range(i, 0, -1):
        print(j, end="")
    print(" ")
    space -= 2
