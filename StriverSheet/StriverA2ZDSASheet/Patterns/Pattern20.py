# [stars, space, stars]
# *                 *     [1,8,1]
# * *             * *     [2,6,2]
# * * *         * * *
# * * * *     * * * *
# * * * * * * * * * *
# * * * *     * * * *
# * * *         * * *
# * *             * *
# *                 *
n = 5
space = 2 * n - 2
for i in range(1, 2*n):
    # stars
    stars = i
    if i > n:
        stars = (2 * n) - i
    for j in range(1,stars+1):
        print("*", end="")
    # Space
    for j in range(1,space+1):
        print(" ", end="")
    # stars
    for j in range(1,stars+1):
        print("*", end="")
    print(" ")
    if i < n:
        space -= 2
    else:
        space += 2
