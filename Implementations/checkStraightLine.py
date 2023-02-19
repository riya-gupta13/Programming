def checkStraightLine(coordinates: list[list[int]]) -> bool:
    # Check if all x or y coordinates are the same
    x_values = [x for x, y in coordinates]
    y_values = [y for x, y in coordinates]
    if len(set(x_values)) == 1 or len(set(y_values)) == 1:
        return True

    # Check for a single line
    slope = None
    for i in range(len(coordinates) - 1):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[i + 1]
        if x1 == x2:
            # Handle vertical lines
            return False
        elif slope is None:
            slope = (y1 - y2) / (x1 - x2)
        else:
            if slope != (y1 - y2) / (x1 - x2):
                return False
    return True


coordinates = [[0,0],[0,1],[0,-1]]

print(checkStraightLine(coordinates))
