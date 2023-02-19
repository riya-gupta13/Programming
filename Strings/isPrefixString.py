def isPrefixString(s: str, words: list[str]) -> bool:
    l = []
    for i in range(1, len(words) + 1):
        new = ''.join(words[0:i])
        l.append(new)
    print(l)
    if s in l:
        return True
    else:
        return False


s = "iloveleetcode"
words = ["i", "love", "leetcode", "apples"]
isPrefixString(s, words)
