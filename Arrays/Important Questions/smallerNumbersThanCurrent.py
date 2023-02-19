def smallerNumbersThanCurrent(nums: list[int]) -> list[int]:
    newList = []
    for i in range(0, len(nums)):
        count = 0
        for j in range(0, len(nums)):
            if nums[j] < nums[i] and j != i:
                count = count + 1
        newList.append(count)
    print(newList)

#     or use dictionary


nums = [8, 1, 2, 2, 3]
# [4,0,1,1,3]
smallerNumbersThanCurrent(nums)
