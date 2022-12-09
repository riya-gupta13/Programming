def fourSum(nums: list[int], target: int) -> list[list[int]]:
    ans = []
    if len(nums) == 0:
        return ans
    nums = sorted(nums)
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            front = j + 1
            back = len(nums) - 1
            tar = target - nums[i] - nums[j]
            while front < back:
                summation = nums[front] + nums[back]
                if summation < tar:
                    front += 1
                elif summation > tar:
                    back -= 1
                else:
                    left = nums[front]
                    right = nums[back]
                    ans.append([nums[i], nums[j], left, right])
                    while front < back and nums[front] == left:
                        front += 1
                    while front < back and nums[back] == right:
                        back -= 1
            while j + 1 < len(nums) and nums[j + 1] == nums[j]:
                j += 1
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
    return ans


nums = [2, 2, 2, 2, 2]
target = 8
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]
print(fourSum(nums, target))

