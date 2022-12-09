def minOperations(nums: list[int]) -> int:
    l = nums
    sum=0
    for i in range(0, len(nums) - 1):
        # print(nums[i + 1],nums[i])
        if nums[i + 1] <= nums[i]:
            sum+= abs(nums[i + 1] - nums[i]) + 1
            l[i + 1] = nums[i + 1] + (abs(nums[i + 1] - nums[i]) + 1)
    print(l,sum)


nums =  [1,1,1]
# Output: 3
minOperations(nums)
