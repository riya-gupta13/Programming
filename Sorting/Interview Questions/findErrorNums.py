def findErrorNums(arr: list[int]):
    i = 0
    while i < len(arr):
        correct = arr[i] - 1
        if arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1
    print(arr)
    ans = []
    for i in range(0, len(arr)):
        if arr[i] != i + 1:
            ans.append(arr[i])
            ans.append(i+1)
    print(ans)

nums = [1, 2, 2]
findErrorNums(nums)
