# only use when we hve numbers from 1 to N

def cycleSort(arr):
    i = 0
    while i < len(arr):
        correct = arr[i] - 1
        if arr[i] != arr[correct]:
            arr[i], arr[correct] = arr[correct], arr[i]
        else:
            i += 1
    print(arr)


# Tc =O(N)
arr = [5, 4, 3, 2, 1]
cycleSort(arr)
