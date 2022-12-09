def relativeSortArray(arr1: list[int], arr2: list[int]):
    ans = []
    for i in arr2:
        while i in arr1:
            ans.append(i)
            arr1.remove(i)
    return ans + sorted(arr1)


arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
arr2 = [2, 1, 4, 3, 9, 6]
relativeSortArray(arr1, arr2)
