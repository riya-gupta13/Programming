def isPerfectSquare(num: int):
    l = 0
    h = num
    while l <= h:
        m = (l + h) // 2
        if m * m == num:
            return True
        elif m * m > num:
            h = m - 1
        else:
            l = m + 1
    return False


print(isPerfectSquare(num=2000105819))
