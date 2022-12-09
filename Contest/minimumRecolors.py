import sys
from itertools import combinations, groupby


def minimumRecolors(blocks: str, k: int) -> int:
    letter = 'B'
    b = letter * k
    print(b)
    l = []
    if b in blocks:
        return 0
    for i in range(0, len(blocks) + 1):
        for j in range(i):
            if len(blocks[j:i]) == k:
                l.append(blocks[j:i])
    print(l)
    m = sys.maxsize
    for i in l:
        c = i.count('W')
        if c < m:
            m = c
    return m


blocks = "WBWBBBW"
k = 2
# Output: 0
print(minimumRecolors(blocks, k))
