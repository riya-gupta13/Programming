def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]:
    ans = []
    for i in range(0, len(nums1)):
        if nums1[i] in nums2:
            ind = nums2.index(nums1[i])
            if ind + 1 >= len(nums2):
                ans.append(-1)
            else:
                if nums2[ind + 1] > nums1[i]:
                    print(nums2[ind + 1])
                    ans.append(nums2[ind + 1])
                else:
                    num = 0
                    for j in nums2[ind + 1:]:
                        if j > nums1[i]:
                            num = j
                            break
                        else:
                            num = -1
                    ans.append(num)
    print(ans)


nums1 = [1, 3, 4, 2]
nums2 = [6, 5, 4, 3, 2, 1, 7]
# Output: [-1,3,-1]
nextGreaterElement(nums1, nums2)
