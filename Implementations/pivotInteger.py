def pivotInteger(n: int) -> int:
    l = []
    for a in range(1, n + 1):
        l.append(a)
    print(l)
    for a in range(n, 0, -1):
        print(l[a:],l[:a-1])
        if sum(l[a:]) == sum(l[:a - 1]):
            return a
    return -1


pivotInteger(8)