def findSubarrays(nums: list[int]) -> bool:
    # for i in range(0, len(nums)):
    #     sumR = 0
    #     sumL = 0
    #     print(nums[:i + 1], nums[i:])
    #     sumL += sum(nums[:i + 1])
    #     sumR += sum(nums[i:])
    #     print(sumR, sumL)
    #     if sumR == sumL and len(nums[:i + 1]) == 2 and len(nums[i:]) == 2:
    #         return True
    # return False

    c = dict()
    for i in range(len(nums) - 1):
        c[nums[i] + nums[i + 1]] = c.get(nums[i] + nums[i + 1], 0) + 1
    return True if max(c.values()) > 1 else False


nums =[1,-1,1,-1,1,-1,1]
print(findSubarrays(nums))
