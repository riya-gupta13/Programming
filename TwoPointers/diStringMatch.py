def diStringMatch(s: str) -> list[int]:
    n = len(s) + 1
    arr = []
    res = []
    for i in range(0, n):
        arr.append(i)
    j = 0
    k = len(arr) - 1
    for i in s:
        if i == 'I':
            res.append(arr[j])
            j += 1
        else:
            res.append(arr[k])
            k = k - 1
    print(res)
    while (j <= len(s) and j <= k):
        res.append(arr[j])
        j += 1
    while (k >= 0 and k >= j):
        res.append(arr[k])
        k -= 1
    print(res)


s="IDID"
Output: [0, 4, 1, 3, 2]
diStringMatch(s)
