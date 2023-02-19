def multiply(num, n):
    ans = 1
    for i in range(n):
        ans *= num
    return ans


def nRoot(n, m):
    l = 0
    h = m
    eps = 1e-6 # for 5 decimal places
    while h - l > eps:
        mid = (l + h) // 2
        if multiply(mid, n) < m:
            l = mid
        else:
            h = mid
    return l
