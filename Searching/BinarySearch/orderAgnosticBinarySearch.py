def orderAgnosticBinarySearch(arr, target):
    s = 0
    e = len(arr) - 1
    isAsc = arr[s] < arr[e]
    # mid = (s + e) // 2
    # instead this we follow below formula why to avoid if s+e exceeds range of int
    # if we solve (s+(e-s))//2, indirectly it is equal to s+e//2 only
    while s <= e:
        mid = (s + e) // 2
        if arr[mid] == target:
            return mid
        if isAsc:
            if target < arr[mid]:
                e = mid - 1
            else:
                s = mid + 1
        else:
            if target > arr[mid]:
                e = mid - 1
            else:
                return -1


arr = [9, 8, 7, 2, 1, 0]
target = 8
print(orderAgnosticBinarySearch(arr, target))
