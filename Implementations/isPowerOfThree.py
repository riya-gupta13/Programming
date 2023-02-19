def isPowerOfThree(n: int) -> bool:
    count = 0
    m = n
    while n > 3:
        if n % 3 == 0:
            count += 1
        n = n // 3
    count += 1
    print(m)
    if 3 ** count == m:
        return True
    else:
        return False


print(isPowerOfThree(27))
