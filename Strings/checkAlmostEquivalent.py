import collections


def checkAlmostEquivalent(word1: str, word2: str) -> bool:
    d1 = collections.Counter(word1)
    d2 = collections.Counter(word2)
    print(d1, d2)
    w = []
    for i in word1:
        if d1[i] - d2[i] <= 3:
            w.append(True)
        else:
            w.append(False)
    for i in word2:
        # print(d2[i],d1[i])
        if d2[i] - d1[i] <= 3:
            w += i
            w.append(True)
        else:
            w.append(False)
    if False in w:
        print(False)
    else:
        print(True)


word1 = "aaaa"
word2 = "bccb"
# Output: false
checkAlmostEquivalent(word1, word2)
