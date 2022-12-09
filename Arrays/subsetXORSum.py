import itertools


def subsetXORSum(nums: list[int]) -> int:
    ct = 0
    for n in range(len(nums) + 1):
        for subset in itertools.combinations(nums, n):
            temp = 0
            for i in subset:
                temp ^= i
            ct += temp
    return ct


nums = [5, 1, 6]
# Output: 6
subsetXORSum(nums)
