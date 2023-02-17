from collections import Counter


def singleNumber(self, nums: list[int]) -> int:
    dict = Counter(nums)
    for key in dict:
        if dict[key] == 1:
            return (key)