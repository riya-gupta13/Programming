def findMiddleIndex(nums: list[int]) -> int:
    ans = -1
    for i in range(0, len(nums)):
        sumL = 0
        sumR = 0
        # print(nums[:i], nums[i + 1:])
        sumL += sum(nums[:i])
        sumR += sum(nums[i + 1:])
        # print(sumL, sumR)
        if sumL == sumR:
            ans = i
            break
        else:
            i += 1
    return (ans)


nums = [2, 3, -1, 8, 4]
# Output: 3
print(findMiddleIndex(nums))
