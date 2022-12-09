def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    nums1.extend(nums2)
    nums1=sorted(nums1)
    mid = len(nums1) / 2
    if len(nums1) % 2 == 0:
        med = (nums1[int(mid - 1)] + nums1[int(mid)]) / 2
    else:
        med = nums1[int(mid)]
    print(med)


# 1234
nums1 = [1, 3]
nums2 = [2]
# Output: 2.00000
findMedianSortedArrays(nums1, nums2)
