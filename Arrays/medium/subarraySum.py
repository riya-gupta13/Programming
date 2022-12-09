def subarraySum(nums: list[int], k: int) -> int:
    # GIVES TLE O(n2)
    count = 0
    for i in range(0, len(nums)):
        sum = 0
        for j in range(i, len(nums)):
            sum += nums[j]
            if sum == k:
                count += 1
    print(count)

    # time complexity is O(n)
    res = {0: 1}
    prefSum = 0
    count = 0
    for i in range(len(nums)):
        prefSum += nums[i]
        if prefSum - k in res:
            count += res[prefSum - k]
        if prefSum not in res:
            res[prefSum] = 0
        res[prefSum] += 1
    return count

nums = [1, -1, 0]
k = 0
subarraySum(nums, k)
# Output: 2
