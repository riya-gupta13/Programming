def findFinalValue(nums: list[int], original: int) -> int:
    while original in nums:
        for i in nums:
            if original == i:
                original *= 2
    return original


nums = [8, 19, 4, 2, 15, 3]
original = 2
# Output: 24
print(findFinalValue(nums, original))
