def maximumWealth(accounts: list[list[int]]) -> int:
    global a
    a = []
    for i in accounts:
        # print(i)
        sum = 0
        for j in range(0, len(i)):
            sum = sum + i[j]
        a.append(sum)
        print(a)
        print(max(a))


accounts = [[1, 5], [7, 3], [3, 5]]
maximumWealth(accounts)
