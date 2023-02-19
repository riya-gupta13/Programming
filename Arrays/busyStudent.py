def busyStudent(startTime: list[int], endTime: list[int], queryTime: int) -> int:
    count = 0
    for j in range(0, len(startTime)):
        for i in range(0, len(endTime)):
            if queryTime <= endTime[i] and startTime[j] <= queryTime and i == j:
                count += 1
    print(count)


# [9,8,7,6,5,4,3,2,1]
# [10,10,10,10,10,10,10,10,10]
# 5
startTime = [9, 8, 7, 6, 5, 4, 3, 2, 1]
endTime = [10, 10, 10, 10, 10, 10, 10, 10, 10]
queryTime = 5
# Output: 1
busyStudent(startTime, endTime, queryTime)
