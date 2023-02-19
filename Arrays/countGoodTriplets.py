def countGoodTriplets(arr: list[int], a: int, b: int, c: int) -> int:
    l=[]
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            for k in range(0, len(arr)):
                if abs(arr[i] - arr[j]) <= a and i < j:
                    if abs(arr[j] - arr[k]) <= b and j < k:
                        if abs(arr[i] - arr[k]) <= c and i < j < k:
                            print(arr[i], arr[j], arr[k])
                            l.append([arr[i], arr[j], arr[k]])
    print(len(l))



arr = [1,1,2,2,3]
a = 0
b = 0
c = 1
# Output: 4
countGoodTriplets(arr,a,b,c)