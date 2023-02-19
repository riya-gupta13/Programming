def maxProduct(nums: list[int]) -> int:
    nums = sorted(nums)
    max=(nums[-2]-1)*(nums[-1]-1)
    print(max)


nums =  [3,7]
# Output: 12
maxProduct(nums)
