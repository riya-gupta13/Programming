# https://takeuforward.org/data-structure/aggressive-cows-detailed-solution/
def aggressiveCows(arr, cows):
    def canPlaceCows(arr, dist, cows):
        placed = arr[0]
        cnt = 1
        for i in range(1, len(arr)):
            if arr[i] - placed >= dist:
                cnt += 1
                placed = arr[i]
                if cnt == cows:
                    return True
        return False

    # n is length of arr or number of stalls
    arr = sorted(arr)
    low = arr[0]
    high = arr[len(arr) - 1] - arr[0]
    while low <= high:
        mid = (low + high) // 2
        if canPlaceCows(arr, mid, cows):
            res = mid
            low = mid + 1
        else:
            high = mid - 1
    return high


arr = [1, 2, 8, 4, 9]
cows = 3
print(aggressiveCows(arr, cows))
