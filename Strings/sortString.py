def sortString(s: str) -> str:
    li = list(s)
    result = set(s)
    print(result)
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    l = []
    res = []
    for i in sorted(result):
        l.append(s.count(i))
    print(l)
    d = dict(zip(sorted(set(s)), l))
    print(d)
    while len(li) != 0:
        for j in alpha:
            if j in li:
                d[j] = d[j] - 1
                res.append(j)
                li.remove(j)
        print(d, res, li)
        for k, v in list(d.items()):
            if v == 0:
                d.pop(k)
        print(d)
        # if not any(d.values()) == False:
        # print(not d)
        if not d == False:
            print(d)
            for i in alpha[::-1]:
                if i in reversed(li):
                    d[i] = d[i] - 1
                    res.append(i)
                    li.remove(i)
            print(d, s, l)
    print("".join(res))


s = "leetcode"
# Output: "abccbaabccba"
sortString(s)
