def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
    low = 0
    high = (len(matrix) * len(matrix[0])) - 1
    m = len(matrix[0])
    while low <= high:
        mid = (low + (high - low) // 2)
        row = int(mid // m)
        col = int(mid % m)
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False