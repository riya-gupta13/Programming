def findGCD(nums: list[int]) -> int:
    maxNum=max(nums)
    minNum=min(nums)
    l=[]
    for i in range(1,minNum+1):
        if maxNum%i==0 and minNum%i==0:
            l.append(i)
    print(l,max(l))



nums =  [3,3]
# Output: 2
findGCD(nums)