# https://leetcode.com/problems/check-if-n-and-its-double-exist/description/
def checkIfExist(arr: list[int]) -> bool:
    # usinh Hashmap
    # just chk whether half or double of that elemnt exists or not
    d = {}
    for val in arr:
        if d.get(val * 2, 0) or d.get(val // 2, 0):
            return True
        d[val] = 1
    return False


def checkIfExistBinary(arr: list[int]) -> bool:
    #     usinh BINARY SEARCH
    arr.sort()
    n = len(arr)
    for i in range(n):
        k = arr[i]

        # binary search for negatives
        if k < 0:
            # only here lo hi chnges as always i>=0
            lo = 0
            hi = i
            while lo < hi:
                mid = (lo + hi) // 2

                if arr[mid] == (2 * k):
                    return True
                elif arr[mid] < (2 * k):
                    lo = mid + 1
                else:
                    hi = mid

        # binary seach for non negatives
        else:
            lo = i + 1
            hi = n
            while lo < hi:
                mid = (lo + hi) // 2

                if arr[mid] == (k * 2):
                    return True
                elif arr[mid] < (k * 2):
                    lo = mid + 1
                else:
                    hi = mid

    return False


arr = [-2, 0, 0, 10, -19, 4, 6, -8]
# Output: true
print(checkIfExist(arr))
