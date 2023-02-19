def myPow(x: float, n: int) -> float:
    ans = 1.0
    power = n
    if power < 0:
        power = -1 * power
    while power > 0:
        if power % 2 == 1:
            ans = ans * x
            power = power - 1
        else:
            x = x * x
            power = power // 2
    if n < 0:
        ans = float(1.0) / float(ans)
    return ans


x = 2.00000
n = -2
print(myPow(x, n))
