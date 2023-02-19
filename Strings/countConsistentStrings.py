def countConsistentStrings(allowed: str, words: list[str]) -> int:
    allow = list(allowed)
    count = []
    for i in words:
        l = set(i)
        if all(j in allow for j in l):
            count.append(i)
    print(len(count))
    return len(count)


allowed = "ab"
words = ["ad", "bd", "aaab", "baa", "badab"]
countConsistentStrings(allowed, words)
