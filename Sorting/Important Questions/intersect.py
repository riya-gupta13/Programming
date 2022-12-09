def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    d = {}
    res = []
    for i in nums1:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for i in nums2:
        if i in d and d[i] > 0:
            res.append(i)
            d[i] -= 1
    print(res)


nums1 = [4, 9, 5, 5, 5]
nums2 = [9, 4, 9, 8, 4, 5, 5]

intersect(nums1, nums2)
