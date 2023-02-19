def numIdenticalPairs(nums: list[int]) -> int:
    count = 0
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if nums[i] == nums[j] and i < j:
                # print(nums[j],nums[j+1])
                count = count + 1
    print(count)
    return count


nums = [1, 2, 3, 1, 1, 3]
# 6
numIdenticalPairs(nums)
