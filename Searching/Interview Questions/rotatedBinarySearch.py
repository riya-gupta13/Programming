def search(nums: list[int], target: int) -> int:
    pivot = rotatedBinarySearch(nums)
    if pivot == -1:
        binarySearch(nums, target, 0, len(nums) - 1)
    if nums[pivot] == target:
        return pivot
    if target >= nums[0]:
        binarySearch(nums, target, 0, pivot - 1)
    return binarySearch(nums, target, pivot + 1, len(nums) - 1)


def binarySearch(arr, target, s, e):
    # mid = (s + e) // 2
    # instead this we follow below formula why to avoid if s+e exceeds range of int
    # if we solve (s+(e-s))//2, indirectly it is equal to s+e//2 only
    while s <= e:
        mid = (s + e) // 2
        # print(mid)
        if target < arr[mid]:
            e = mid - 1
        elif target > arr[mid]:
            s = mid + 1
        else:
            return mid
    return -1


# findPivot
def rotatedBinarySearch(nums: list[int]):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if mid > start and nums[mid] < nums[mid - 1]:
            return mid - 1
        elif mid < end and nums[mid] > nums[mid + 1]:
            return mid
        if nums[mid] <= nums[start]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


# # findPivot for dupliactes
def rotatedBinarySearchWithDuplicates(nums):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if mid > start and nums[mid] < nums[mid - 1]:
            return mid - 1
        elif mid < end and nums[mid] > nums[mid + 1]:
            return mid

        # if elements at middle, start, end are equal then just skip the duplicates
        if nums[mid] == nums[start] and nums[mid] == nums[end]:
            # skip the duplicates
            # NOTE: what if these elements at start and end were the pivot??
            # check if start is pivot
            if start < end and nums[start] > nums[start + 1]:
                return start
            start += 1

            # check whether end is pivot
            if end > start and nums[end] < nums[end - 1]:
                return end - 1
            end -= 1
        #  left side is sorted, so pivot should be in right
        elif nums[start] < nums[mid] or nums[start] == nums[mid] and nums[mid] > nums[end]:
            start = mid + 1
        else:
            end = mid - 1

    return -1
