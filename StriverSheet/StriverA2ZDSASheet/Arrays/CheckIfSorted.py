def check(nums: list[int]) -> bool:
    flag = -1
    for i in range(len(nums) - 1):
        if nums[i] > nums[i + 1]:
            flag = i
            break
    print(flag)
    arr = nums[flag + 1:] + nums[0:flag + 1]
    print(arr)
    if flag == -1:
        return True
    return sorted(nums) == arr
nums = [2,1,3,4]
check(nums)