def nextPermutation(nums: list[int]) -> None:
    if len(nums) <= 1:
        return
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            for k in range(len(nums) - 1, i, -1):
                if nums[k] > nums[i]:
                    nums[i], nums[k] = nums[k], nums[i]
                    nums[i + 1:] = sorted(nums[i + 1:])
                    break
            break
        else:
            if i == 0:
                nums.sort()
    print(nums)

nums = [1,3,2]
# Output: [1,3,2]
nextPermutation(nums)
