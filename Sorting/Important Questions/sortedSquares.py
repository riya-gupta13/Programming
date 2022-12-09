def sortedSquares(nums: list[int]):
    # In the above algorithm, we reverse the output which is a O(n) operation.
    # Which can be avoided by creating a result list of the same length with dummy values
    # (I'm taking 0s here but this doesn't actually matter).
    # The thing to keep in mind is that, we're finding the largest values one by one.
    # So we have to fill the result from the right end, or the starting index will be len(nums) - 1.
    # We keep decrementing this value as we add more values to the result
    l, r = 0, len(nums) - 1
    res = [0] * len(nums)  # create a result list with dummy values
    i = len(nums) - 1  # index on which we will fill the result
    while l <= r:
        if abs(nums[l]) > abs(nums[r]):
            res[i] = nums[l] ** 2
            l += 1
        else:
            res[i] = nums[r] ** 2
            r -= 1
        i -= 1  # we have filled the result on this index, now we go to the index one lesser than this
    return res
