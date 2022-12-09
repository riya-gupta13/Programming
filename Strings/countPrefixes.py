def countPrefixes(words: list[str], s: str) -> int:
    pr = s[0]
    print(pr)
    count = 0
    for w in words:
        if s.startswith(w):
            count += 1
    print(count)


words = ["a","b","c","ab","bc","abc"]
s = "abc"
countPrefixes(words, s)
