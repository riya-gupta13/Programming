def plusOne(digits: list[int]) -> list[int]:
    st = 1
    new = 0
    for i in digits:
        # new=(new*10)+i
        new += st * i
        st *= 10
    e = new + 1
    ans=[]
    for i in str(e):
        ans.append(int(i))
    print(ans)


digits = [4, 2, 3]
plusOne(digits)
