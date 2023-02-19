def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    j = len(nums)
    for i in range(0, len(nums)):
        if nums[i] == 0:
            nums.insert(j, nums[i])
            nums.remove(nums[i])
