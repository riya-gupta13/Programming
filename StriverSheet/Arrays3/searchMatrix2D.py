def searchMatrix(matrix: list[list[int]], target: int) -> bool:
    # row = []
    # for i in range(0, len(matrix)):
    #     for j in range(0, len(matrix[0])):
    #         if j == 0:
    #             if target >= matrix[i][j]:
    #                 row = matrix[i]
    # print(row)
    # for k in range(0, len(row)):
    #     if row[k] == target:
    #         return True
    # else:
    #     return False

    low = 0
    high = (len(matrix) * len(matrix[0])) - 1
    if not len(matrix):
        return False
    m = len(matrix[0])
    while low <= high:
        mid = (low + (high - low)// 2)
        print(mid)
        row = int(mid // m)
        col = int(mid % m)
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]]

target = 3
# Output: true
print(searchMatrix(matrix, target))
