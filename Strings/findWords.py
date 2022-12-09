def findWords(words: list[str]) -> list[str]:
    first = "qwertyuiop"
    second = "asdfghjkl"
    third = "zxcvbnm"
    l = []
    for i in words:
        if all(j in list(first) for j in i.lower()):
            print("first", i)
            l.append(i)
        if all(j in second for j in i.lower()):
            print("second", i)
            l.append(i)
        if all(j in third for j in i.lower()):
            print("third", i)
            l.append(i)
    print(l)


words = ["adsdf", "sfd"]
# Output: ["Alaska","Dad"]
findWords(words)
