def pivotIndex(nums: list[int]) -> int:
    leftSum = 0
    rightSum = sum(nums)
    counter = 0
    for x in nums:
        rightSum -= x
        if leftSum == rightSum:
            return counter
        leftSum += x
        counter += 1

    return -1

nums = [1,7,3,6,5,6]
# Output: 3