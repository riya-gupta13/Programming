def transpose(matrix: list[list[int]]):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transpose(matrix)
