def convertToTitle(columnNumber: int) -> str:
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = []
    while columnNumber != 0:
        temp = (columnNumber - 1) % 26
        res.append(alpha[temp])
        columnNumber = (columnNumber - 1) // 26
    return "".join(res[::-1])


print(convertToTitle(columnNumber=701))
