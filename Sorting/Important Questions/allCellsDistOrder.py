def allCellsDistOrder(rows: int, cols: int, rCenter: int, cCenter: int):
    # approach we will make an array with all coordinates then we will find ditnce with cnter then sort
    def distance(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

    points = []
    for i in range(rows):
        for j in range(cols):
            points.append((i, j))

    center = [rCenter, cCenter]
    points.sort(key=lambda c: distance(c, center))

    return points


rows = 1
cols = 2
rCenter = 0
cCenter = 0
allCellsDistOrder(rows, cols, rCenter, cCenter)
