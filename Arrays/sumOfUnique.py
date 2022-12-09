def sumOfUnique(nums: list[int]) -> int:
    sum=0
    for i in range(0, len(nums)):
        c = nums.count(nums[i])
        if c == 1:
            print(nums[i], c)
            sum+=nums[i]
    print(sum)



nums = [1,2,3,4,5]
# Output: 4
sumOfUnique(nums)