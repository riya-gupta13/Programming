def largestPerimeter(nums: list[int]) -> int:
    nums.sort(reverse=True)
    while len(nums) > 2 and nums[0] >= nums[1] + nums[2]:
        nums.pop(0)
    if len(nums) < 3:
        return 0
    else:
        return sum(nums[:3])



