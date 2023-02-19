def countNegatives(grid: list[list[int]]) -> int:
    collen = len(grid[0])
    rowlen = len(grid)
    i = rowlen - 1
    j = 0
    total = 0
    while i >= 0 and j < collen:
        if grid[i][j] < 0:
            total += collen - j
            i -= 1
        else:
            j += 1
    return total


grid = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
print(countNegatives(grid))
