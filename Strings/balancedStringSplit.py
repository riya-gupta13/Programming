def balancedStringSplit(s: str) -> int:
    count = 0
    n = []
    res = 0
    for x in s:
        if 'R' in x:
            count = count - 1
            n.append(count)
        if 'L' in x:
            count = count + 1
            n.append(count)
    for x in n:
        if 0 == x:
            res = res + 1
    print(res)


s = "RLRRLLRLRL"
# Output: 4
balancedStringSplit(s)
