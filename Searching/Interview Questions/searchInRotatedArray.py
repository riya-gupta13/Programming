def search(self, nums: list[int], target: int) -> int:
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid

        if nums[l] <= nums[mid]:  # means we are in  left sorted portion
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        # means we are in  right sorted portion
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return -1


nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
