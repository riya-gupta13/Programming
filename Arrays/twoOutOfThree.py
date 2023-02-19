import collections


def twoOutOfThree(nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
    n = min(len(nums1), len(nums2), len(nums3))
    n1 = {}
    n2 = {}
    n3 = {}
    for i in nums1:
        n1[i] = nums1.count(i)
    for i in nums2:
        n2[i] = nums2.count(i)
    for i in nums3:
        n3[i] = nums3.count(i)
    print(n1, n2, n3)
    l = []
    for i in n1.keys():
        if i in n2.keys():
            l.append(i)
        if i in n3.keys():
            l.append(i)
    for i in n2.keys():
        if i in n1.keys() or i in n3.keys():
            l.append(i)
    for i in n3.keys():
        if i in n1.keys() or i in n2.keys():
            l.append(i)
    print(set(l))


nums1 = [1, 2]
nums2 = [2, 3]
nums3 = [3]
# nums1 = [3,1]
# nums2 = [2,3]
# nums3 = [1,2]
# nums1 = [1,2,2]
# nums2 = [4,3,3]
# nums3 = [5]
# Output: [3,2]
twoOutOfThree(nums1, nums2, nums3)
