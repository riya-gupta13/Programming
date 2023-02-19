def firstMissingPositive(arr: list[int]) -> int:
    i = 0
    # using cyclic sort as numbers [0,n], diff value ==index
    while i < len(arr):
        correct = arr[i] - 1
        if 0 < arr[i] <= len(arr) and arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1
    print(arr)
    for j in range(0, len(arr)):
        if j+1 != arr[j]:
            return j + 1
    return len(arr) + 1


arr = [1, 2, 0]
print(firstMissingPositive(arr))
