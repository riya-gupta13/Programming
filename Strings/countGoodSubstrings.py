def countGoodSubstrings(s: str) -> int:
    l = []
    for i in range(0, len(s)+1):
        for j in range(i):
            if len(s[j:i]) == 3:
                l.append(s[j:i])
    count = 0
    print(l)
    for j in l:
        if len(set(j)) == len(j):
            count += 1
    print(count)


s = "aababcabc"
# Output: 1
countGoodSubstrings(s)
