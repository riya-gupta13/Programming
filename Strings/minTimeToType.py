def minTimeToType(word: str) -> int:
    l = list(word)
    res = len(l)
    w = 'a'
    for i in l:
        k = abs(ord(i) - ord(w))
        if k > 13:
            k = 26 - k
        res += k
        w = i
    return res


word = "bza"
# Output: 7
minTimeToType(word)
