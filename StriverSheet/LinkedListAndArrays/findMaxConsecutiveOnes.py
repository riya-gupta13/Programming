def findMaxConsecutiveOnes(nums: list[int]) -> int:
    count = 0
    maxi = 0
    for i in range(0, len(nums)):
        if nums[i] == 1:
            count += 1
        else:
            count = 0
        maxi = max(maxi, count)
    return maxi


nums = [1, 0, 1, 1, 0, 1]
# Output: 3
print(findMaxConsecutiveOnes(nums))
