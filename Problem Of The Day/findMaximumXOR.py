def findMaximumXOR(nums: list[int]) -> int:
    max = 0
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            xor = nums[i] ^ nums[j]
            if max <= xor:
                max = xor
    print(max)


nums = [14]
# Output: 28
findMaximumXOR(nums)
