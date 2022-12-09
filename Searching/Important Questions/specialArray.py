# https://leetcode.com/problems/special-array-with-x-elements-greater-than-or-equal-x/
def specialArray(nums: list[int]) -> int:
    low = 0
    high = 1000

    while low <= high:
        mid = (low + high) // 2
        count = 0
        for current_number in nums:
            if current_number >= mid:
                count = count + 1
        if mid == count:
            return mid
        elif mid < count:
            low = mid + 1
        elif mid > count:
            high = mid - 1

    return -1
