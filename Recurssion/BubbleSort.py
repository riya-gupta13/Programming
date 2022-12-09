def BubbleSort(arr, r, c):
    if r == 0:
        return
    if c < r:
        if arr[c] > arr[c + 1]:
            arr[c], arr[c + 1] = arr[c + 1], arr[c]
        BubbleSort(arr, r, c + 1)
    else:
        BubbleSort(arr, r - 1, 0)


arr = [4, 3, 2, 1]
BubbleSort(arr, len(arr) - 1, 0)
print(arr)
