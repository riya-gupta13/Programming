def sortColors(nums: list[int]):
    low = 0
    high = len(nums) - 1
    mid = 0
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1

        elif nums[mid] == 1:
            mid += 1
        else:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1
    print(nums)


nums = [1,2,0]
sortColors(nums)
