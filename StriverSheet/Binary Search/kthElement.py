# https://practice.geeksforgeeks.org/problems/k-th-element-of-two-sorted-array1317/1
# not submitting yet getting TLE
def kthElement(arr1, arr2, n, m, k):
    # approach we have to use binary search -now e have to find a partition where left portion's elements are less
    # than right portion evn if we combine the arrays so how can we reach there, wht well do find mid and less than
    # tht values should be on left anf greater thn tht on right if it's not then we move left if in left its greater
    # else move right but there are some edge cases consider low should always be in range k-m as if k=len(m) thn it
    # should not be like we take all elements of frst array second edge case if k>len(n) so we should always tke min(
    # k,n) as high edge case can tht mid we are comparing can go out of range so we will tke care of it
    if n > m:
        return kthElement(arr2, arr1, m, n, k)
    low = max(0, k - m)
    high = min(k, n)
    while low <= high:
        cut1 = (low + high) // 2
        cut2 = k - cut1
        l1 = float("-inf") if cut1 == 0 else arr1[cut1 - 1]
        l2 = float("-inf") if cut2 == 0 else arr2[cut2 - 1]
        r1 = float("inf") if cut1 == n else arr1[cut1]
        r2 = float("inf") if cut2 == m else arr2[cut2]

        if l1 <= r2 and l2 <= r1:
            return max(l1, l2)
        elif l1 > r2:
            high = cut1 - 1
        else:
            low = cut1 + 1
    return -1


arr1 = [2, 3, 6, 7, 9]
arr2 = [1, 4, 8, 10]
k = 5
