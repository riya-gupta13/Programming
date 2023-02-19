import sys
from itertools import combinations


def maximumRobots(chargeTimes: list[int], runningCosts: list[int], budget: int) -> int:
    n = len(chargeTimes)
    a = []
    l = []
    for i in range(0, len(chargeTimes) + 1):
        for j in range(i):
            a.append(chargeTimes[j:i])
    for i in range(0, len(runningCosts) + 1):
        for j in range(i):
            l.append(chargeTimes[j:i])
    print(l)
    # while n != 0:
    #     a.extend(list(combinations(chargeTimes, n)))
    #     n -= 1
    # print(a)
    total = 0
    maximum = 0
    for i in range(0,len(a)):

        # print(i,runningCosts[strt:end + 1])
        total = max(a[i]) + len(a[i]) * sum(l[i])
        # print(total)

        if total <= budget and maximum < len(i):
            print(i)
            maximum = len(i)
        # print(maximum)
    return maximum


chargeTimes = [3, 6, 1, 3, 4]
runningCosts = [2, 1, 3, 4, 5]
budget = 25
# Output: 3
print(maximumRobots(chargeTimes, runningCosts, budget))
