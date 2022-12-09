def targetIndices(nums: list[int], target: int) -> list[int]:
    numbers = sorted(nums)
    res = []
    for n in range(0, len(sorted(nums))):
        if numbers[n] == target:
            res.append(n)
    print(res)


nums = [1, 2, 5, 2, 3]
target = 2
# Output: [3]
targetIndices(nums, target)
