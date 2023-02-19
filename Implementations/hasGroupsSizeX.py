from collections import Counter


def hasGroupsSizeX(deck: list[int]) -> bool:
    if len(deck) == 1:
        return False
    d = Counter(deck)
    print(d)
    print([i > 1 for i in d.values()], len(set(d.values())) == 1)
    if [i > 1 for i in d.values()][0]:
        if len(set(d.values())) == 1:
            return True
        else:
            return False
    return False


deck = [1, 1, 2, 2, 2, 2]
print(hasGroupsSizeX(deck))
