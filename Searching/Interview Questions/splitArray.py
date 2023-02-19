# https://leetcode.com/problems/split-array-largest-sum/

def splitArray(nums: list[int], k: int) -> int:
    start = 0
    end = 0
    # range is decided like this because min value of subarray can be max item in array and end can be sum of all
    # items of array
    for i in range(0, len(nums)):
        start = max(start, nums[i])  # in the end of the loop this will contain the max item of the array
        end += nums[i]

    # why we using binary search here because we hve a range of values where we need to find ans, we can use binary
    # search binary search
    while start < end:
        # try for the middle as potential ans
        mid = start + end // 2
        # calculate how many pieces you can divide this in with this max sum
        sum = 0
        pieces = 1
        for i in nums:
            if sum + i > mid:
                # means we cannot add more element to that subarray, new subarray
                # say you add this num to new sum, then sum=num
                sum = i
                pieces += 1
            else:
                sum += i
        if pieces > mid:
            start = mid + 1
        else:
            end = mid
    return end  # here start == end
