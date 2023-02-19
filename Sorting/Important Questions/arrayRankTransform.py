def arrayRankTransform(arr: list[int]):
    c = 1
    d = dict()
    for i in sorted(list(set(arr))):
        d[i] = c
        c += 1
    for i in range(len(arr)):
        arr[i] = d[arr[i]]
    return arr


arr = [37, 12, 28, 9, 100, 56, 80, 5, 12]
arrayRankTransform(arr)
