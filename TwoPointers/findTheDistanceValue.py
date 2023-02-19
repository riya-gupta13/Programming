def findTheDistanceValue(arr1: list[int], arr2: list[int], d: int):
    res = []
    for i in range(0, len(arr1)):
        flag = 0
        for j in range(0, len(arr2)):
            if abs(arr1[i] - arr2[j]) > d:
                flag += 1
                if flag == len(arr2):
                    res.append(arr1[i])
    print(len(res))
    return len(res)


def findTheDistanceValue2(arr1: list[int], arr2: list[int], d: int):
    res = []
    i = arr1[0]
    j = arr2[0]
    flag = 0
    k = 0
    while k != len(arr1):
        if abs(arr1[i] - arr2[j]) > d:
            flag += 1
            j += 1
            if flag == len(arr2):
                res.append(arr1[i])
        i += 1
        k += 1

    print(len(res))

arr1 = [2, 1, 100, 3]
arr2 = [-5, -2, 10, -3, 7]
d = 6
findTheDistanceValue2(arr1, arr2, d)
