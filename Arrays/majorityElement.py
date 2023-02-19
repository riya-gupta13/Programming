import collections


def majorityElement(nums: list[int]) -> int:
    dct2 = collections.Counter(nums)
    print(dct2)
    for i in dct2:
        if dct2[i] > len(nums) / 2:
            return i


nums = [2, 2, 1, 1, 1, 2, 2]
Output: 3
print(majorityElement(nums))
