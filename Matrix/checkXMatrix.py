def checkXMatrix(grid: list[list[int]]) -> bool:
    m = len(grid)
    sum = 0
    flag = False
    flags = False
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if i == j or i == m - 1 - j:
                print("Diagonal", grid[i][j])
                if grid[i][j] != 0:
                    flag = True
                    print("hi", i, j)
                else:
                    return False
            if i != j and i + j != m - 1:
                # print("others", grid[i][j])
                if grid[i][j] == 0:
                    flags = True
                    print("hi", i, j)
                else:
                    return False
    if flag is True and flags is True:
        return True
    else:
        return False


grid = [[5, 0, 0, 1], [0, 4, 1, 5], [0, 5, 2, 0], [4, 1, 0, 2]]
# Output: true
print(checkXMatrix(grid))
