def twoSum(nums: list[int], target: int) -> list[int]:
    dict = {}
    res = []
    for i in range(0, len(nums)):
        if (target - nums[i]) in dict.keys():
            res.append(dict[target - nums[i]])
            res.append(i)
            return res
        else:
            dict.__setitem__(nums[i], i)
    return res


nums = [3,3]
target = 6
# Output: [0,1]
print(twoSum(nums,target))
