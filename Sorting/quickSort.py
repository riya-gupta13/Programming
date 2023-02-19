def quickSort(arr, low, high):
    if low >= high:
        return
    start = low
    end = high

    mid = start + (end - start) // 2
    pivot = arr[mid]
    while start <= end:
        while arr[start] <= pivot:
            start += 1
        while arr[end] > pivot:
            end += 1
        if start <= end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    print(arr)


arr = [5, 4, 3, 2, 1]
quickSort(arr, 0, len(arr) - 1)

# TC: o(NLOGN), WORST(O(n^2))