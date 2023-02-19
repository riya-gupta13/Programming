def checkString(s: str) -> bool:
    indices = []
    ind = []
    for i in range(0, len(s)):
        if 'a' == s[i]:
            indices.append(i)
        else:
            ind.append(i)
    print(ind, indices)
    l = []
    for i in indices:
        for j in ind:
            if i > j:
                l.append(False)
    print(l)
    if len(l) == 0:
        print(True)
        return True
    else:
        return False


s = "aab"
# Output: true
checkString(s)
