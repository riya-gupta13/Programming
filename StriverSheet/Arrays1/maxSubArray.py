def maxSubArray(nums: list[int]) -> int:
    sum = 0
    max = float('-inf')
    s = 0
    l = []
    for i in range(0, len(nums)):
        sum += nums[i]
        if sum > max:
            l = []
            max = sum
            l.append(s)
            l.append(i)
        if sum < 0:
            sum = 0
            s = i + 1
    print(max, l)


nums = [5, 4, -1, 7, 8]
# Output: 6
maxSubArray(nums)
