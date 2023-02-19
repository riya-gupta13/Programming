def duplicateZeros(arr: list[int]):
    temp = []
    x = 0
    for i in range(0, len(arr)):
        if arr[i] != 0:
            temp.insert(x, arr[i])
            x += 1
        else:
            temp.insert(x, 0)
            temp.insert(x + 1, 0)
            x += 2
    a = temp[:len(arr)]
    print(arr)
    arr = a.copy()
    print(arr)


def duplicateZerosTwoPointer(arr: list[int]):
    x = len(arr)
    j = 0
    while j < x:
        if arr[j] == 0:
            while arr[j] == 0:
                arr.insert(j + 1, 0)
                arr.pop(-1)
                j = j + 2
                if j >= x:
                    break
        j += 1


arr = [1, 0, 2, 3, 0, 4, 5, 0]
# Output: [1,0,0,2,3,0,0,4]
duplicateZeros(arr)
