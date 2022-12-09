
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
def searchRangeBest(self, nums: list[int], target: int) -> list[int]:
    n = len(nums)
    if n == 0:
        return [-1, -1]
    l = 0
    h = n - 1
    a = []
    ans = -1
    # For checking the leftmost index
    while l <= h:
        m = (l + h) >> 1
        if nums[m] == target:
            ans = m
            h = m - 1  # to find left most we'll traverse left
        elif nums[m] > target:
            h = m - 1
        else:
            l = m + 1
    # For checking the rightmost index
    a.append(ans)
    l = ans
    h = n - 1
    while l <= h:
        m = (l + h) >> 1
        if nums[m] == target:
            ans = m
            l = m + 1
        elif nums[m] < target:
            l = m + 1
        else:
            h = m - 1
    a.append(ans)
    return a


# One binary search searches for the left most index, whenever we find the target, we "mark" it as the potential
# answer and continue binary searching left.
# Same logic for the other side, whenever we find the target we "mark" and continue searching right.
# In the end we return the best matches we found in each binary search.
# This will perform 2 binary searches as 2*log(n) which is asymptotically O(logn)
# Note: we could exit after 1 binary search if we didn't find any target in our array. Both indexes will be [-1, -1]

def searchRange(self, nums: list[int], target: int):
    left_target_index = self.binary_search_on_left(nums, target, 0, len(nums) - 1)
    if left_target_index == -1:
        return [-1, -1]

    right_target_index = self.binary_search_on_right(nums, target, 0, len(nums) - 1)
    return [left_target_index, right_target_index]


def binary_search_on_left(self, nums: list[int], target: int, left: int, right: int):
    index_on_left = -1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            index_on_left = mid

        if nums[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1

    return index_on_left


def binary_search_on_right(self, nums: list[int], target: int, left: int, right: int):
    index_on_right = -1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            index_on_right = mid

        if nums[mid] <= target:
            left = mid + 1
        else:
            right = mid - 1

    return index_on_right


Color=("red","blue")
print(Color[0])