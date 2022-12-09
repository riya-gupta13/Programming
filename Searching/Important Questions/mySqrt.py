def mySqrt(x: int) -> int:
    lo, hi = 0, x
    while True:
        n = lo + (hi - lo) // 2
        if n * n <= x < (n + 1) * (n + 1):
            return n
        elif x < n * n:
            hi = n - 1
        else:
            lo = n + 1


