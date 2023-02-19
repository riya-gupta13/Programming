# https://leetcode.com/problems/first-bad-version/
def firstBadVersion(n: int) -> int:
    left = 1
    right = n
    while left <= right:
        mid = round((left + right) / 2)
        if isBadVersion(mid):
            if not isBadVersion(mid - 1):
                return int(mid)
            right = mid - 1
        else:
            left = mid + 1
    return int(mid)


n = 4
firstBadVersion(n)
