def permutation(r, c=''):
    if len(r) == 0:
        print(c)
    for i in range(0, len(r)):
        newC = c + r[i]
        newR = r[0:i] + r[i + 1:]
        permutation(newR, newC)


l = []
str = "abcd"
print(permutation(str))

