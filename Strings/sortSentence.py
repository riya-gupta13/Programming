def sortSentence(s: str) -> str:
    s = s.split()
    l = len(s) + 1
    new_i = [None] * l
    for x in range(0, len(s)):
        index = int(s[x][-1])
        new_i[index] = s[x][:-1]
    if None in new_i:
        new_i.remove(None)
    print(" ".join(new_i))


s = "is2 sentence4 This1 a3"
# Output: "Me Myself and I"
sortSentence(s)
