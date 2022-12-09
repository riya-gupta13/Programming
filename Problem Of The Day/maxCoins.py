def maxCoins(nums: list[int]) -> int:
    coins = 0
    for i in range(1, len(nums)):
        if len(nums) == 2:
            coins += nums[0] * nums[1]
            coins += nums[1]
            break
        if len(nums) == 1:
            coins += nums[1]
        while len(nums) != 2:
            coins += nums[i - 1] * nums[i] * nums[i + 1]
            nums.remove(nums[i])
    print(coins)


nums = [9, 76, 64, 21]
# Output: 167
maxCoins(nums)
