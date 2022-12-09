def countEven(num: int) -> int:
    ans = []
    for i in range(1, num+1):
        s = str(i)
        sum = 0
        for j in s:
            sum += int(j)
        if sum % 2 == 0:
            ans.append(i)
    print(len(ans))


num = 30
# Output: 2
countEven(num)
