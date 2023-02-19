def missingNumber(arr: list[int]) -> int:
    i = 0
    # using cyclic sort as numbers [0,n], diff value ==index
    while i < len(arr):
        correct = arr[i]
        if arr[i] < len(arr) and arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1
    print(arr)
    for j in range(0, len(arr)):
        if j != arr[j]:
            return j
    return len(arr)


arr = [3, 0, 1]
print(missingNumber(arr))
