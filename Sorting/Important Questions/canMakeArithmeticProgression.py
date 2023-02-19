def canMakeArithmeticProgression(arr: list[int]) -> bool:
    arr=sorted(arr)
    dif=arr[1]-arr[0]
    if all(arr[i+1]-arr[i]==dif for i in range(0,len(arr)-1)):
        print(True)
    else:
        print(False)


arr = [2,1,4]
# Output: true
canMakeArithmeticProgression(arr)