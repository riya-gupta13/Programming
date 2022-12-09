def peakIndexInMountainArray(arr: list[int]) -> int:
    for i in range(0,len(arr)-1):
        while not arr[i]<arr[i+1]:
            return (i)



arr = [0,6,7,1]
# Output: 1
print(peakIndexInMountainArray(arr))