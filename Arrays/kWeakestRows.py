from operator import itemgetter


def kWeakestRows(mat: list[list[int]], k: int) -> list[int]:
    l = []
    l1 = []
    for i in range(0, len(mat)):
        l.append([i, sum(mat[i])])
    l2 = sorted(l, key=itemgetter(1))
    print(l)
    for i in l2:
        l1.append(i[0])
    print(l1[:k])


mat = [[1, 1, 0, 0, 0],
       [1, 1, 1, 1, 0],
       [1, 0, 0, 0, 0],
       [1, 1, 0, 0, 0],
       [1, 1, 1, 1, 1]]
k = 3
# Output: [2,0,3]
kWeakestRows(mat, k)
