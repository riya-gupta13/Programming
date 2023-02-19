import numpy as np


def diagonalSum(mat: list[list[int]]) -> int:
    # m=np.matrix(mat)
    # print(m)
    # diag=m.diagonal()
    # print(diag)
    n = len(mat)
    mid = n // 2
    sum = 0
    for i in range(n):
        sum += mat[i][i]
        sum += mat[n - i - 1][i]
    if n % 2 != 0:
        sum -= mat[mid][mid]
    print(sum)


mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
# Output: 25
diagonalSum(mat)
