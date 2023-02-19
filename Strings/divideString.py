def divideString(s: str, k: int, fill: str) -> list[str]:
    l = []
    j = k
    for i in range(0, len(s), j):
        new = s[i:j]
        l.append(new)
        j += k
    print(l)
    final = []
    for j in l:
        if len(j) < k:
            r = ''
            diff = k - len(j)
            print(diff)
            for i in range(0, diff):
                r = j + fill
                j = r
            final.append(r)
        else:
            final.append(j)
    print(final)


s = "abcdefgh"
k = 3
fill = "x"
divideString(s, k, fill)
