def minTimeToVisitAllPoints(points: list[list[int]]) -> int:
    total = 0
    for i in range(0, len(points) - 1):
        p1 = points[i]
        p2 = points[i + 1]
        total += max(abs(p2[0] - p1[0]), abs(p2[1] - p1[1]))
    print(total)


points = [[1, 1], [3, 4], [-1, 0]]
# Output: 7
minTimeToVisitAllPoints(points)
