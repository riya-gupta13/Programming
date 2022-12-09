def createTargetArray(nums: list[int], index: list[int]) -> list[int]:
    l = []
    for i in range(0,len(nums)):
        l.insert(index[i], nums[i])
    print(l)



nums = [0,1,2,3,4]
index = [0,1,2,2,1]
# Output: [0,4,1,3,2],[0,1,2,3,4]
createTargetArray(nums, index)
