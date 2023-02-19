def rotate(matrix: list[list[int]]) -> None:
    n = len(matrix[0])
    # as rows and cols are equal
    for row in range(n):
        print(row)
        for col in range(row, n):
            matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]
    for i in range(len(matrix)):
        matrix[i].reverse()
    print(matrix)


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(matrix)
