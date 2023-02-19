import collections


def shortestCompletingWord(licensePlate: str, words: list[str]) -> str:
    al = ''
    for i in licensePlate:
        if i.lower().isalpha():
            al += i.lower()
    print(al)
    c = collections.Counter(al)
    # print(c)
    words.sort(key=len)
    for word in words:
        w = collections.Counter(word)
        print(c - w)
        if not (c - w):
            return word


licensePlate = "1s3 PSt"
words = ["step", "steps", "stripe", "stepple"]
shortestCompletingWord(licensePlate, words)
