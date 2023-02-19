# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        * [1,7,1]
# **      **[2,5,2]
# ***    ***[3,3,3]
# ****  ****[4,1,4]
# **********[5,0,5]

n = 5
spaces = 0

for i in range(n):
    # numbers
    for j in range(1, n - i + 1):
        print("*", end="")
    # space
    for j in range(spaces):
        print(" ", end="")
    # numbers
    for j in range(1, n - i + 1):
        print("*", end="")
    print(" ")
    spaces += 2
spaces = spaces - 2
for i in range(1, n + 1):
    # numbers
    for j in range(1, i + 1):
        print("*", end="")
    # space
    for j in range(spaces):
        print(" ", end="")
    # numbers
    for j in range(1, i + 1):
        print("*", end="")
    spaces -= 2
    print(" ")
