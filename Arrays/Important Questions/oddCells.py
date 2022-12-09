import numpy as np


def oddCells(m: int, n: int, indices: list[list[int]]) -> int:
    mat = np.zeros((m, n), dtype=np.int32)
    # print(mat)
    sum = 0
    for row, col in indices:
        # print(row,col)
        for i in range(n):
            mat[row][i] += 1
        for i in range(m):
            # print(mat[i][col])
            mat[i][col] += 1
    print(mat)
    for i in range(m):
        for j in range(n):
            if mat[i][j] % 2 != 0:
                sum += 1
    print(sum)
    # return sum(1 for i in range(m) for j in range(n) if mat[i][j] % 2 != 0)


m = 2
n = 3
indices = [[0, 1], [1, 1]]
# Output: 6
oddCells(m, n, indices)
