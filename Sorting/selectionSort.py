def selectionSort(arr):
    for i in range(0, len(arr)):
        min = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        if min != i:
            arr[i], arr[min] = arr[min], arr[i]
    return arr


arr = [3, 1, 5, 4, 2]
print(selectionSort(arr))
# TC: O(n^2)
