def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
    nums1 = set(nums1)
    nums2 = set(nums2)
    n = nums1.intersection(nums2)
    return (list(n))


#  we can use hashtable too
def intersectionHashTable(self, nums1: list[int], nums2: list[int]) -> list[int]:
    res = []
    map = {}
    for i in nums1:
        map[i] = map[i] + 1 if i in map else 1
    for j in nums2:
        if j in map and map[j] > 0:
            res.append(j)
            map[j] = 0

    return res
