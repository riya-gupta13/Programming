# https://www.interviewbit.com/problems/matrix-median/

def findMedian(A):
    low = 0
    high = 1e9
    n = len(A)
    m = len(A[0])
    while low <= high:
        mid = (low + high) // 2
        cnt = 0
        # for every row count
        for i in range(n):
            cnt += countNumbersSmallerThanEqualToMid(A[i], mid)
        if cnt <= (n * m) // 2:
            low = mid + 1
        else:
            high = mid - 1
    return low


def countNumbersSmallerThanEqualToMid(row, mid):
    l = 0
    h = len(row) - 1
    while l <= h:
        md = (l + h) // 2
        if row[md] <= mid:
            l = mid + 1
        else:
            h = mid - 1
    return l
