def search(arr, target):
    n = len(arr)
    if n != 0:
        if arr[0] == target:
            return True
        return search(arr[1:], target)
    return False


arr = [2, 3, 9,18]
print(search(arr, 18))
