def findDisappearedNumbers(arr: list[int]):
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
            ans.append(i+1)
    print(ans)


nums =[4,3,2,7,7,2,3,1]
findDisappearedNumbers(nums)
