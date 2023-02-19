ans = False


def sortArray(arr):
    global ans
    n = len(arr)
    if n != 1:
        if arr[0] <= arr[1]:
            ans = True
            sortArray(arr[1:])
        else:
            ans = False
            return ans
    return ans


arr = [1, 2, 3, 4, 8, 9, 0]
print(sortArray(arr))
