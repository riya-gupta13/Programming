import math


def isUgly(num):
    if num <= 0:
        return False
    while num != 1:
        for divisor in (2, 3, 5):
            if num % divisor == 0:
                num = num // divisor
                break
        else:
            return False
    return num == 1

print(isUgly(8))
