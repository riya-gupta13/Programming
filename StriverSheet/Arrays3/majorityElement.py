def majorityElement(nums: list[int]) -> int:
    count = 0
    element = 0
    for i in nums:
        if count == 0:
            element = i
        if i == element:
            count += 1
        else:
            count -= 1
    return element


nums = [3, 3, 4]
print(majorityElement(nums))
