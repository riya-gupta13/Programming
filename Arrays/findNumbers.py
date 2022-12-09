def findNumbers(nums: list[int]) -> int:
    l = []
    for i in nums:
        count = 0
        while i!=0:
            i=i//10
            count+=1
        l.append(count)
    dig=0
    for i in l:
        if i%2==0:
            dig+=1
    print(dig)


nums = [555,901,482,1771]
# Output: 2
findNumbers(nums)
