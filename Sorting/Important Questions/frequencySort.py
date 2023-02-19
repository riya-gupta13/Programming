from collections import Counter


def frequencySort(nums: list[int]):
    count = Counter(nums)
    # here - denotes that if count equal then dec order
    return sorted(nums, key=lambda x: (count[x], -x))


nums = [1, 1, 2, 2, 2, 3]
print(frequencySort(nums))
