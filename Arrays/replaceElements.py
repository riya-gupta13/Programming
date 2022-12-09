def replaceElements(arr: list[int]) -> list[int]:
    for i in range(0, len(arr)):
        if i + 1 >= len(arr):
            arr[-1] = -1
        else:
            arr[i] = max(arr[i + 1:])
    print(arr)


arr = [17, 18, 5, 4, 6, 1]
# Output: [18,6,6,6,1,-1]
replaceElements(arr)
