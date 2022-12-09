def floor(arr, target):
    s = 0
    e = len(arr) - 1
    
    while s <= e:
        mid = (s + e) // 2
        # print(mid)
        if target < arr[mid]:
            e = mid - 1
        elif target > arr[mid]:
            s = mid + 1
        else:
            return mid
    return e


arr = [2, 4, 9, 14, 16, 18]
target = 15
print(floor(arr, target))
