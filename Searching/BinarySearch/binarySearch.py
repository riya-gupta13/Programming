def binarySearch(arr, target):
    s = 0
    e = len(arr) - 1
    # mid = (s + e) // 2
    # instead this we follow below formula why to avoid if s+e exceeds range of int
    # if we solve (s+(e-s))//2, indirectly it is equal to s+e//2 only
    while s <= e:
        mid = (s + e) // 2
        # print(mid)
        if target < arr[mid]:
            e = mid - 1
        elif target > arr[mid]:
            s = mid + 1
        else:
            return mid
    return -1


arr = [0, 2, 4, 6, 7, 8, 9]
target = 8
print(binarySearch(arr, target))
