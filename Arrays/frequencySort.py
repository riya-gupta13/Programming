import collections
from operator import itemgetter


def frequencySort(nums: list[int]) -> list[int]:
    d = collections.Counter(nums)
    print(d)
    s = sorted(d.values())
    new = sorted(d.items(), key=itemgetter(1))
    print(dict(new))


nums = [2, 3, 1, 3, 2]
# Output: [3,1,1,2,2,2]
frequencySort(nums)
