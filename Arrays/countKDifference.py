def countKDifference(nums: list[int], k: int) -> int:
    count = 0
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if abs(nums[j] - nums[i]) == k and i < j:
                count += 1
    print(count)


nums = [3, 2, 1, 5, 4]
k = 2
# Output: 4
countKDifference(nums, k)
