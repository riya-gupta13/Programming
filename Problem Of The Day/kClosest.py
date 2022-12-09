def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
    l = []
    for i in points:
        for j in range(0, len(i) - 1):
            diff = (i[j] ** 2) + (i[j + 1] ** 2)
            l.append(diff)
    l = sorted(l)
    l = l[:k]
    res=[]
    for i in points:
        for j in range(0, len(i) - 1):
            if (i[j] ** 2) + (i[j + 1] ** 2) in l:
                res.append([i[j], i[j + 1]])
    return res


points = [[3, 3], [5, -1], [-2, 4]]
k = 2
# Output: [[-2,2]], [[3,3],[-2,4]]
# (i.e., √(x1 - x2)2 + (y1 - y2)2)
kClosest(points, k)
