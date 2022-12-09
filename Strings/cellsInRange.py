def cellsInRange(s: str) -> list[str]:
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabets = list(alpha)
    print(alphabets)
    nums = '123456789'
    numbers = list(nums)
    print(numbers)
    l = list(s)
    col = []
    row = []
    for i in l:
        if i in alphabets:
            col.append(i)
        if i in numbers:
            row.append(i)
    print(col, row)
    row = sorted(row)
    col = sorted(col)
    print(col, row)
    start = alpha.index(col[0])
    print(start)
    end = alpha.index(col[1])
    print(end)
    cols = alphabets[start:end + 1]
    print(cols)
    startRow = nums.index(row[0])
    endRow = nums.index(row[1])
    rows = numbers[startRow:endRow + 1]
    res = []
    for i in rows:
        for j in cols:
            res.append(j + i)
    print(sorted(set(res)))


s = "B1:F6"
# ["K1","K2","L1","L2"]
cellsInRange(s)
