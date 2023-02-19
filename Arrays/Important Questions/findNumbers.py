def findNumbers(self, nums: list[int]) -> int:
    count = 0
    for i in range(0, len(nums)):
        num = str(nums[i])
        if len(num) % 2 == 0:
            count += 1
    return count