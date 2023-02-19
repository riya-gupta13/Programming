def searchRange(nums: list[int], target: int) -> list[int]:
    ans = []
    for i in range(0, len(nums)):
        if nums[i] == target:
            ans.append(i)
    if not ans:
        return [-1, -1]
    if len(ans) == 1:
        ans.append(ans[0])
        return ans
    else:
        return ans
    # print(ans)


nums =[3,3,3]

target = 3
print(searchRange(nums, target))
# Output: [3,4]
