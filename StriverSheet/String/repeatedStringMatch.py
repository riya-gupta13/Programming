def repeatedStringMatch(self, a: str, b: str) -> int:
    strA = a
    count = 1
    repeat = len(b) // len(a)
    for i in range(repeat + 2):
        if a.__contains__(b):
            return count
        else:
            a += strA
            count += 1
    return -1