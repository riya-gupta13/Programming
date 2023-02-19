def mergesortedArray(nums1: list[int], m: int, nums2: list[int], n: int):
    # nums1.extend(nums2)
    # print(nums1)
    # nums1 = sorted(nums1)
    # print(nums1)
    # # return nums1[], nums1[:n + 1]
    k = 0
    if len(nums1) == 0:
        return sorted(nums2)
    if len(nums2) == 0:
        return sorted(nums1)
    for i in range(0, len(nums1)):
        if nums1[i] > nums2[k]:
            nums1[i], nums2[k] = nums2[k], nums1[i]
            nums2 = sorted(nums2)
    nums1 = nums1[:m]
    nums2 = nums2[:n]
    nums1[m+1:]=nums2[:n]
    print(nums1)


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
mergesortedArray(nums1, m, nums2, n)
