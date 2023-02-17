def isBoomerang(points: list[list[int]]) -> bool:
    if points[0] == points[1] or points[0] == points[2] or points[1] == points[2]:
        return False
    (x1, y1) = points[0]
    (x2, y2) = points[1]
    (x3, y3) = points[2]
    if (y2 - y1) * (x3 - x2) == (y3 - y2) * (x2 - x1):
        return False
    return True