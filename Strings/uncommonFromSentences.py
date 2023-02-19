import collections


def uncommonFromSentences(s1: str, s2: str) -> list[str]:
    d1 = collections.Counter(s1.split())
    print(d1)
    d2 = collections.Counter(s2.split())
    print(d2)
    l = []
    for i in d1.keys():
        if i not in d2.keys() and d1[i] == 1:
            print(i)
            l.append(i)
    for i in d2.keys():
        if i not in d1.keys() and d2[i] == 1:
            print(i)
            l.append(i)
    print(l)


s1 = "this apple is sweet"
s2 =  "this apple is sour"
# s2 = "this apple is sour"
# Output: ["sweet","sour"]
uncommonFromSentences(s1, s2)
