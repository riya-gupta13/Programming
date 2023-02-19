def maxProduct(nums: list[int]) -> int:
    nums = sorted(nums)
    maxP = (nums[-2] - 1) * (nums[-1] - 1)
    print(maxP)
