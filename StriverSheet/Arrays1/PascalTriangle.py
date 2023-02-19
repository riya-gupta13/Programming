def PascalTriangle(numRows):
    previousRow = []
    res = []
    for i in range(0, numRows):
        row = []
        for j in range(0, i+1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(previousRow[j - 1] + previousRow[j])
        previousRow = row
        res.append(row)
    return(res)


numRows = 7
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
PascalTriangle(numRows)
