def removeDuplicates(nums: list[int]) -> int:
    for i in range(0, len(nums)):
        for j in range(1, len(nums)):
            if nums[i] == nums[j]:
                nums[j] = '_'

    count = 0
    for i in nums:
        if i != '_':
            count += 1
    print(nums, count)


nums = [1, 1, 2]
# Output: 2
# nums = [1, 2, _]
removeDuplicates(nums)
