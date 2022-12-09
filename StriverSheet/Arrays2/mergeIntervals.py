def merge(intervals: list[list[int]]):
    # ans = []
    # intervals = sorted(intervals)
    # for i in range(0, len(intervals) - 1):
    #     if intervals[i][1] >= intervals[i + 1][0]:
    #         m = max(intervals[i][1], intervals[i + 1][1])
    #         ans.append([intervals[i][0], m])
    #     else:
    #         ans.append(intervals[i + 1])
    # print(ans)

    if len(intervals) == 1:
        return intervals
    intervals.sort()
    temp = intervals[0]
    ans = []
    for i in range(1, len(intervals)):
        if intervals[i][0] <= temp[1]:
            temp[1] = max(temp[1], intervals[i][1])
        else:
            ans.append(temp)
            temp = intervals[i]
    ans.append(temp)
    return ans


intervals = [[1,3],[2,6],[5,9],[8,10],[15,18]]
Output: [[1, 6], [8, 10], [15, 18]]
print(merge(intervals))
