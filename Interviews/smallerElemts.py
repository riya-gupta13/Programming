def smallerElemnt(arr):
    ans = {}
    for i in range(0, len(arr)):
        count = 0
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                count += 1
        ans.__setitem__(arr[i],count)
    print(ans)

array=[8,4,5,2,1]
smallerElemnt(array)
