def smallestEqual(nums: list[int]) -> int:
    l = []
    for i in range(0, len(nums)):
        if i % 10 == nums[i]:
            l.append(i)
    if len(l) == 0:
        print(-1)
    else:
        print(min(l))


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# Output: 0
smallestEqual(nums)
