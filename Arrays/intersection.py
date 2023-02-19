def intersection(nums1: list[int], nums2: list[int]) -> list[int]:
    nums1 = set(nums1)
    nums2 = set(nums2)
    n = nums1.intersection(nums2)
    print(list(n))


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
intersection(nums1, nums2)
