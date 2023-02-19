def DigitProd(n):
    # if n%10==n:return n
    if n == 0:
        return 0
    return n % 10 * DigitProd(n // 10)



