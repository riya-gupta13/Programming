import collections


def containsDuplicate(nums: list[int]):
    d=collections.Counter(nums)
    if set(d.values())!={1}:
        return True
    return False
