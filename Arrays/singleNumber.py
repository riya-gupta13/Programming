from collections import Counter


def singleNumber(nums: list[int]) -> int:
    dict = Counter(nums)
    print(dict)
    for key in dict:
        if dict[key] == 1:
            print(key)


nums = [-4, 0, 0]
# Output: 1
singleNumber(nums)
