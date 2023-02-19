def findKthLargest(nums: list[int], k: int) -> int:
    nums.sort()
    return nums[len(nums) - k]


# By quickSelect
def findKthLargest2(nums: list[int], k: int) -> int:
    # algo --- QUICK SELECT similar to quick sort we will take pivot as last element and then compare, and we will
    # take a pointer p and swap with then move forward filling the array but at end the elements greater thn pivot at
    # same position so wht we do is we swap p with pivot, so now we have array which contains all elements lesser thn
    # pivot on left and on rght all greater than we chk if k<p then it lies on left otherwise on right but if it is
    # equal to p then we return tht as we know it will be largest kth as left smaller and right are the greatest so

    k = len(nums) - k

    def quickSelect(l, r):
        pivot = nums[r]
        p = l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]

        if p > k:
            return quickSelect(l, p - 1)
        elif p < k:
            return quickSelect(p + 1, r)
        else:
            return nums[p]

    return quickSelect(0, len(nums) - 1)


nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4
print(findKthLargest(nums, k))
