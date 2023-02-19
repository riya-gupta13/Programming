import numpy as np


def transpose(matrix: list[list[int]]):
    m = len(matrix)
    n = len(matrix[0])
    if n != m:
        temp = np.ones(shape=(n, m), dtype=int)
    else:
        temp = np.ones(shape=(m, n), dtype=int)

    for i in range(0, len(temp)):
        for j in range(0, len(temp[0])):
            print(i, j)
            temp[i][j] = matrix[j][i]
    print(temp)


matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[1,4,7],[2,5,8],[3,6,9]]
transpose(matrix)
