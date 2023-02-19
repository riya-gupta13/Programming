def subsetsWithDup(nums: list[int]) -> list[list[int]]:
    nums = sorted(nums)
    res = []

    def backtrack(i, subset):
        if i == len(nums):
            res.append(subset[::])
            return
        subset.append(nums[i])
        backtrack(i + 1, subset)
        subset.pop()
        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        backtrack(i + 1, subset)

    backtrack(0, [])
    return res


nums = [1, 2, 2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
