def rotatedBinarySearch(arr, target, start, end):
    if start > end:
        return -1
    mid = start + (end-start)//2
    if arr[mid] == target:
        return mid
    if arr[start] <= arr[mid]:
        if arr[start] <= target <= arr[mid]:
            return rotatedBinarySearch(arr, target, start, mid - 1)
        else:
            return rotatedBinarySearch(arr, target, mid + 1, end)
    if arr[end] >= target >= arr[mid]:
        return rotatedBinarySearch(arr, target, mid + 1, end)
    return rotatedBinarySearch(arr, target, start, mid - 1)


arr = [5, 6, 7, 8, 9, 1, 2, 3]
print(rotatedBinarySearch(arr, 5, 0, len(arr) - 1))
