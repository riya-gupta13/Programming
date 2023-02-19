def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    if k == 0:
        return nums

    # compute rotation
    k = k % len(nums)
    lenght = len(nums)

    # swap positions
    nums[lenght - k:], nums[:lenght - k] = nums[:lenght - k], nums[lenght - k:]