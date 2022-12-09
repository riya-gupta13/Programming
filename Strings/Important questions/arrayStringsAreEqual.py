def arrayStringsAreEqual(word1: list[str], word2: list[str]) -> bool:
    w = "".join(word1)
    w2 = "".join(word2)
    if w == w2:
        return True
    else:
        return False


word1 = ["abc", "d", "defg"]
word2 = ["abcddefg"]
# Output: true
arrayStringsAreEqual(word1, word2)
