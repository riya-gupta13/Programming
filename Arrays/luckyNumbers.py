def luckyNumbers(matrix: list[list[int]]) -> list[int]:
    ans=0
    n = len(matrix)
    m = len(matrix[0])
    for i in range(n):
        min1 = matrix[i][0]
        index = 0
        for j in range(m):
            if matrix[i][j] < min1:
                min1 = matrix[i][j]
                index = j
        max1 = matrix[i][index]
        for x in range(n):
            if matrix[x][index] > max1:
                max1 = matrix[x][index]
        if max1 == min1:
            ans.append(max1)

    return ans


matrix = [[3,6],[7,1],[5,2],[4,8]]
# Output: [15]
luckyNumbers(matrix)
