def moveZeroes(nums: list[int]):
    j = len(nums)
    for i in range(0, len(nums)):
        if nums[i] == 0:
            nums.insert(j, nums[i])
            nums.remove(nums[i])
            print(nums)
    print(nums)


nums = [0,0,0, 1, 2, 3]
moveZeroes(nums)
