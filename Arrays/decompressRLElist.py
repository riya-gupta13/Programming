def decompressRLElist(nums: list[int]) -> list[int]:
    newList = []
    l=[]
    for i in range(0, len(nums) - 1,2):
        newList.append([nums[i],nums[i+1]])
    print(newList)
    for n in newList:
        for m in range(0,n[0]):
            l.append(n[1])
    print(l)
    return l


nums = [1, 1, 2, 3]
# Output: [2,4,4,4]
decompressRLElist(nums)
# 
