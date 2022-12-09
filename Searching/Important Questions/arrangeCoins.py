# https://leetcode.com/problems/arranging-coins/
def arrangeCoins(n: int) -> int:
    # approach
    # we will find coins by the formula (n*(n+1))//2
    l = 1
    h = n
    res = 0
    while l <= h:
        mid = (l + h) // 2
        coins = (mid / 2) * (mid + 1)
        if coins > n:
            h = mid - 1
        else:
            l = mid + 1
            res = max(mid, res)
    return res


arrangeCoins(8)
