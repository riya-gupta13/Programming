def minDeletionSize(strs: list[str]) -> int:
    res = 0
    for i in range(len(strs[0])):
        lst = []
        for row in strs:
            lst.append(row[i])
        if lst != sorted(lst):
            res += 1
    return res


strs = ['a', 'b']
# Output: 1
minDeletionSize(strs)
