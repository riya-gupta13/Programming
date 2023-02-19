def linearSearch(arr, target):
    if len(arr) == 0:
        return -1
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i
    return -1


# TC O(N), best O(1)

def linearSearchInString(str, target):
    if len(str) == 0:
        return False
    if target in str:
        return True
    return False
