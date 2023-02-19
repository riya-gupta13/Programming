def sortedSquares(nums: list[int]) -> list[int]:
    l=[]
    for i in nums:
        l.append(i**2)
    print(sorted(l))


nums = [-4, -1, 0, 3, 10]
# Output: [0, 1, 9, 16, 100]
sortedSquares(nums)