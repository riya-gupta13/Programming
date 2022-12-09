def rotate(nums: list[int], k: int) -> None:
    nums[:] = nums[-(k % len(nums)):] + nums[:-(k % len(nums))]


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
# Output: [5,6,7,1,2,3,4]
rotate(nums, k)
