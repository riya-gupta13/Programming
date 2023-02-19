def merge(nums1: list[int], m: int, nums2: list[int], n: int):
    i = m - 1
    j = n - 1
    k = m + n - 1
    while i >= 0 and j >= 0:
        if nums2[j] >= nums1[i]:
            nums1[k] = nums2[j]
            j = j - 1
            k = k - 1
        elif nums2[j] < nums1[i]:
            nums1[k] = nums1[i]
            i = i - 1
            k = k - 1
    while i >= 0:
        nums1[k] = nums1[i]
        k = k - 1
        i = i - 1
    while j >= 0:
        nums1[k] = nums2[j]
        j = j - 1
        k = k - 1
    print(nums1)