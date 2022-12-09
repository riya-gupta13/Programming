def maxProductDifference(nums: list[int]) -> int:
    n=sorted(nums)
    diff = abs((n[0]*n[1])-(n[-1]*n[-2]))
    print(diff)



nums = [4,2,5,9,7,4,8]
# Output: 34
maxProductDifference(nums)
