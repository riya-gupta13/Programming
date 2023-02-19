def runningSum(nums: list[int]):
    new_arr = []
    sum = 0
    temp = 0
    for n in range(0, len(nums)):
        sum = sum + nums[n]
        new_arr.append(sum)
    print(new_arr)
    return new_arr


nums = [3, 1, 2, 10, 1]
runningSum(nums)
