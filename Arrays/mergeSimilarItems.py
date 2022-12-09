import collections


def mergeSimilarItems(items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
    d = {}
    for i in items1:
        d.setdefault(i[0], (i[1]))
    print(d)
    for j in items2:
        x = j[0]
        if x in d.keys():
            d[x] += j[1]
        else:
            d.__setitem__(j[0], j[1])
    d = sorted(d.items(), key=lambda item: item[0])
    print(d)
    ans = []
    for i in d:
        ans.append([i[0], i[1]])
    print(ans)


items1 = [[1,3],[2,2]]
items2 = [[7,1],[2,2],[1,4]]
# Omutput: [[1,6],[3,9],[4,5]]
mergeSimilarItems(items1, items2)
