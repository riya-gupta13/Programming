def findDisappearedNumbers(self, arr: List[int]) -> List[int]:
    i = 0
    while i < len(arr):
        correct = arr[i] - 1
        if arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1
    ans = []
    for i in range(0, len(arr)):
        if arr[i] != i + 1:
            ans.append(i + 1)
    return (ans)
