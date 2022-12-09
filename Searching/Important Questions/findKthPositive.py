# https://leetcode.com/problems/kth-missing-positive-number/
def findKthPositive(arr: list[int], k: int) -> int:
    # approach we will frst try to find the count of missing numbers in range--> last elemnt-len(arr) will give count
    # other case can be that missing number lies outside range [1,2,3,4], so in this case we will do
    # last elmnt +k-countOfMissing
    l = 0
    h = len(arr) - 1

    def compute(actual, expected):
        return actual - expected

    missing = compute(arr[h], len(arr))

    while l <= h:
        mid = (l + h) // 2
        # as consider [2,3,6,9,11]--->arr[mid]=6(actual), expected-(3)
        missing = compute(arr[mid], mid + 1)
        if missing >= k:
            h = mid - 1
        else:
            l = mid + 1
    if h == -1:
        return k
    return arr[h] + k - compute(arr[h], h + 1)
