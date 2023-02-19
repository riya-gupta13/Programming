# A
# BB
# CCC
# DDDD
# EEEEE

n = 5

for i in range(0, n):
    ch = 65 + i
    for j in range(i + 1):
        print(chr(ch), end="")
    print(" ")
