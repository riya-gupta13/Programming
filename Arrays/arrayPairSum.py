from itertools import combinations


def arrayPairSum(nums: list[int]) -> int:
    nums = sorted(nums)
    l = tuple(zip(nums[0::2], nums[1::2]))
    m = 0
    for i in l:
        m += min(i)
    print(m)


nums = [6, 2, 6, 5, 1, 2]
# Output: 4
arrayPairSum(nums)
