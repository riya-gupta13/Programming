def bubbleSort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    print(arr)

# TC: O(n^2), bestCase O(N-1)
# SC: O(1)
arr = [3, 1, 5, 4, 2]
bubbleSort(arr)
