def sunOfDigits(n):
    sum = 0
    while n != 0:
        rem = n % 10
        sum += rem
        n = n // 10
    print(sum)


# with recrssioin
def sumOfDigitsR(n):
    if n < 0:
        return -1
    if n == 0:
        return 0
    else:
        # 182----18
        r = n // 10
        # 182 -- 2
        s = n % 10
        return s + sumOfDigitsR(r)
