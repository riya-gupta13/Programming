def sortArrayByParityII(nums: list[int]) -> list[int]:
    l=[]
    li=[]
    for i in range(0, len(nums)):
        if nums[i] % 2 == 0:
            l.append(nums[i])
        else:
            li.append(nums[i])
    res=[]
    for i in range(0,len(l)):
        res.append(l[i])
        res.append(li[i])
    print(res)


nums = [2,3,5,6]
# Output: [4,5,2,7]
sortArrayByParityII(nums)
