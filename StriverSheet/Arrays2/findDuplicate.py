def findDuplicate(nums: list[int]) -> int:
    # floyd's tortoise
    slow = nums[0]
    fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    fast = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow


nums = [1, 3, 1, 4, 2]
print(findDuplicate(nums))

nums = [1, 3, 4, 2, 2]
Output: 2
