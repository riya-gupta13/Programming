def nextGreaterElement(nums1, nums2):
    ans = []
    for i in nums1:
        ind = nums2.index(i)
        s = nums2[ind+1:]
        # s = num[::-1]
        print(s)
        for j in s:
            # print(j)
            if j > i:
                ans.append(j)
                break
        else:
            ans.append(-1)
    print(ans)


# [7,7,7,7,7]
nums1 = [4, 1, 2]
nums2 = [1, 3, 4, 2]
nextGreaterElement(nums1, nums2)
