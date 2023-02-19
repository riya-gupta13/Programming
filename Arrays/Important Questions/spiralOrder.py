def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
    result = []
    if not matrix:
        return result
    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, 0
    while row < rows and col < cols:
        for i in range(col, cols):
            result.append(matrix[row][i])
        row += 1
        for i in range(row, rows):
            result.append(matrix[i][cols - 1])
        cols -= 1
        if row < rows:
            for i in range(cols - 1, col - 1, -1):
                result.append(matrix[rows - 1][i])
            rows -= 1
        if col < cols:
            for i in range(rows - 1, row - 1, -1):
                result.append(matrix[i][col])
            col += 1
    return result