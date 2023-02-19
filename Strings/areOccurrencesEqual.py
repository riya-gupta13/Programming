def areOccurrencesEqual(s: str) -> bool:
    l = set(s)
    res = []
    for i in l:
        count = s.count(i)
        res.append(count)
    print(res)
    if len(set(res)) == 1:
        print("true")
    else:
        print("false")


s = "a"
# Output: false
areOccurrencesEqual(s)
