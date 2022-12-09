def longestNiceSubstring(s: str) -> str:
    l = []
    for i in range(0, len(s) + 1):
        for j in range(i):
            if len(s[j:i]) >= 2:
                l.append(s[j:i])
    print(l)
    # for i in l:
    #     for j in i:
    #         if j


s = "YazaAay"
# Output: "aAa"
longestNiceSubstring(s)
