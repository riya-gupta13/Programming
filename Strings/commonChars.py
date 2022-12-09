def commonChars(words: list[str]) -> list[str]:
    l = list(words[0])
    # print(l)
    for i in words:
        k = []
        for j in i:
            if j in l:
                k.append(j)
                l.remove(j)
        l = k
    print(l)
    # return l


words = ["bella", "label", "roller"]
# Output: ["e","l","l"]
commonChars(words)
