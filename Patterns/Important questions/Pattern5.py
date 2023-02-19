# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *
n = 5
for i in range(2*n+1):
    stars = i
    # print(i)
    if i > n:
        stars = (2 * n) - i
    for j in range(stars + 1):
        print("*", end="")
    print(" ")

