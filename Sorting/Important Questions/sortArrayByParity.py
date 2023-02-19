def sortArrayByParity(nums: list[int]) -> list[int]:
    l = []
    li = []
    for i in range(0, len(nums)):
        if nums[i] % 2 == 0:
            l.append(nums[i])
        else:
            li.append(nums[i])
    l.extend(li)
    print(l, li)




nums = [7, 9, 8, 5, 4, 2, 1]
# Output: [2,4,3,1]
sortArrayByParity(nums)
