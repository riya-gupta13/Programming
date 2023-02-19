def minSubsequence(nums: list[int]) -> list[int]:
    nums.sort(reverse=True)
    for i in range(len(nums) + 1):
        print(nums[:i],sum(nums[i:]))
        if sum(nums[:i]) > sum(nums[i:]):
            print(nums[:i])


nums = [4, 3, 10, 9, 8]
# Output: [10,9]
minSubsequence(nums)
