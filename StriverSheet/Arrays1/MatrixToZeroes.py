def matrixToZero(matrix):
    global r, c
    m = len(matrix)
    n = len(matrix[0])
    row = [1] * m
    col = [1] * n

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if matrix[i][j] == 0:
                row[i] = 0
                col[j] = 0
    for i in range(0, len(matrix)):
        if row[i] == 0:
            matrix[i] = [0] * n
    print(matrix)
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            if col[j] == 0:
                matrix[i][j] = 0
    print(matrix)


matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]

Output: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]
matrixToZero(matrix)
