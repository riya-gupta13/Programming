def searchInsert(nums: list[int], target: int) -> int:
    l = 0
    h = len(nums) - 1
    while l <= h:
        mid = (l + h) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            h = mid - 1
    return l


nums = [1, 3, 5, 6]
target = 7
print(searchInsert(nums, target))
