def repeatMissing(arr):
    ans = []
    print(arr)
    sum1 = sum(arr)
    print(sum1)
    n = len(arr)
    s = n * (n + 1) // 2
    arr2 = list(set(arr))
    sum2 = sum(arr2)
    print(arr2, sum2)
    rep_num = sum1 - sum2
    ans.append(rep_num)
    ans.append(s - sum2)
    return ans


arr = [3, 1, 2, 5, 4, 6, 7, 5]
print(repeatMissing(arr))
