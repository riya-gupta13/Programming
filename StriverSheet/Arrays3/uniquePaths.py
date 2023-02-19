def uniquePaths(m: int, n: int) -> int:
    # DP APPROACH
    # def rec(m, n, dp)
    #
    #     if i >= m or j >= n:
    #         return 0

    res = 1
    N = m + n - 2
    r = m - 1
    for i in range(1, r + 1):
        res = res * (N - r + i) // i
    return res


m = 3
n = 2
# Output: 28
print(uniquePaths(m, n))
