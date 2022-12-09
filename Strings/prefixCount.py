def prefixCount(words: list[str], pref: str) -> int:
    out=[]
    for i in words:
        if i.startswith(pref):
            print(i)
            out.append(i)
    print(len(out))


words = ["pay","attention","practice","attend"]
pref = "at"
# 2
prefixCount(words,pref)