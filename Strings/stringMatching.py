def stringMatching(words: list[str]) -> list[str]:
    l=[]
    for i in range(0, len(words)):
        for w in words[i + 1:]:
            if words[i].__contains__(w):
                l.append(w)
            if w.__contains__(words[i]):
                l.append(words[i])
    print(l)


words = ["blue","green","bu"]
# Output: ["as","hero"]
stringMatching(words)
