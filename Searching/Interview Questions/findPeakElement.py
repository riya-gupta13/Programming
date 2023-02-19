def findPeakElement(arr: list[int]):
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if arr[mid] > arr[mid + 1]:
            #  you are in dec part of array
            #  this may be the ans, but look at left
            #  this is why end != mid - 1
            end = mid
        else:
            #  you are in asc part of array
            start = mid + 1
    return start

