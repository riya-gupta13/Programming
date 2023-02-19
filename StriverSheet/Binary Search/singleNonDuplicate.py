def singleNonDuplicate(nums: list[int]) -> int:
    # approach we can observe that we need to find breakpoint where it is appearing once so if we notice that bfore
    # breakpoint all elemnts in left hlf are evn index frst instance secnd on odd and opp on rght so wht will we do
    # is we will find mid and chk mid is ven or odd based on tht well find its instance and then move l and h,
    # we will be lnding at end at a point where h will just bfore the breakpoint(left hlf) and rght will be just aftr
    # teh brekpoint(rght hlf) and low will be ans

    # for left half
    # even index--- frst instance
    # odd index-- scnd---i need to chk if thge frst instance of tht num is there or not
    l = 0
    h = len(nums) - 2
    while l <= h:
        mid = (l + h) // 2.
        # we r doing xor as consider if u r at odd index to chk if left we will chk prev index
        # so we do xor of odd woth 1 it gives even and opp for even thst why we use xor operator
        if nums[mid] == nums[mid ^ 1]:
            l = mid + 1
        else:
            h = mid - 1
    return nums[l]


nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
singleNonDuplicate(nums)
