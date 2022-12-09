def longestConsecutive(nums: list[int]) -> int:
    set1 = set(nums)
    current = 0
    long = 0
    streak = 0
    for i in nums:
        if not i - 1 in set1:
            current = i
            streak = 1
        while current + 1 in set1:
            current = current + 1
            streak += 1
        long = max(long, streak)
    return long


nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# Output: 4
print(longestConsecutive(nums))
