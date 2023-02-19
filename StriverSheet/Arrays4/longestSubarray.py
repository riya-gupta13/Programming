def largestSubarray(nums, n):
    dict = {}
    sum = 0
    maximum = 0
    for i in range(0, len(nums)):
        sum += nums[i]
        if sum == 0:
            maximum = i + 1
        else:
            if sum in dict.keys():
                maximum = max(maximum, i - dict[sum])
            else:
                dict.__setitem__(sum, i)
    return maximum

N = 5
array = [1, 3, -5, 6, -2]
print(largestSubarray(array, N))
