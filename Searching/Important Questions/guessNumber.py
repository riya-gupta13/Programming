def guess(num):
    pick = 1
    if num > pick:
        return -1
    elif num < pick:
        return 1
    else:
        return 0


def guessNumber(n: int) -> int:
    lo = 0
    hi = n
    while lo <= hi:
        mid = (lo + hi) // 2
        if guess(mid) == -1:
            hi = mid - 1
        elif guess(mid) == 1:
            lo = mid + 1
        else:
            return mid


print(guessNumber(2))
