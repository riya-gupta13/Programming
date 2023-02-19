from math import lcm


def subarrayLCM(nums: list[int], k: int) -> int:
    cnt = 0
    for i in range(0, len(nums)):
        l = nums[i]
        for j in range(i, len(nums)):
            l = lcm(l, nums[j])
            if l == k: cnt += 1
            if l > k: break

    return cnt


nums = [3, 6, 2, 7, 1]
k = 6
subarrayLCM(nums, k)
