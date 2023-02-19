def addToArrayForm(num: list[int], k: int) -> list[int]:
    n = ""
    for i in num:
        n += str(i)
    nums = int(n)
    print(nums)
    addition = nums + k
    ans=addition
    res=[]
    for i in str(ans):
        res.append(int(i))
    print(res)





num = [2,1,5]
k = 806
addToArrayForm(num, k)
