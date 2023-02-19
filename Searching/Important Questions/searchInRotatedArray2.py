def search(nums: list[int], target: int) -> bool:
    l = 0
    r = len(nums) - 1
    while l <= r:
        while l < r and nums[l + 1] == nums[l]:
            l += 1
        while l < r and nums[r - 1] == nums[r]:
            r -= 1
        mid = (l + r) // 2
        if target == nums[mid]:
            return True
        if nums[l] <= nums[mid]:
            if target > nums[mid] or target < nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        else:
            if target < nums[mid] or target > nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    return False
