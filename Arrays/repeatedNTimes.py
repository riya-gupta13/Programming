def repeatedNTimes(nums: list[int]) -> int:
    for i in range(0,len(nums)):
        c=nums.count(nums[i])
        if c>1:
            print(nums[i],c)
            return nums[i]



nums = [1,8,3,8]
# Output: 3
print(repeatedNTimes(nums))

