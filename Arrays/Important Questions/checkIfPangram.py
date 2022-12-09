import collections


def checkIfPangram(sentence: str) -> bool:
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    d = collections.Counter(sentence)
    out = "".join(d.keys())
    if all(x in out for x in alphabets):
        return True
    else:
        return False


sentence = "leetcode"
print(checkIfPangram(sentence))
