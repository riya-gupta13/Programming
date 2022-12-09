def jobSequencing(Jobs, n):
    jobs = Jobs.sort(key=lambda i: i.profit)
    jobs = jobs[::-1]
    profit = 0
    count = 0
    result = [False] * 100
    for i in range(0, n):
        for j in range(jobs[i].deadline - 1, -1, -1):
            if not result[j]:
                result[j] = True
                profit = jobs[i].profit
                count += 1
                break
    return profit, count


N = 5
Jobs = [(1, 2, 100), (2, 1, 19), (3, 2, 27),
        (4, 1, 25), (5, 1, 15)]
jobSequencing(Jobs, N)
