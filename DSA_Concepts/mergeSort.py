def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]
        mergeSort(left)
        mergeSort(right)
        merge(left, right)


def merge(left, right):
    i = j = k = 0
    new = []
    if left[i] < right[j]:
        new[k] = left[i]
        k += 1
        i += 1
    else:
        new[k] = right[j]
        k += 1
        j += 1
    while (i < len(left)):
        new[k] = left[i]
        k += 1
        i += 1
    while (j < len(right)):
        new[k] = right[j]
        k += 1
        j += 1
    return new


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    print(mergeSort(arr))
