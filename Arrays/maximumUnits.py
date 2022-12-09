from operator import itemgetter


def maximumUnits(boxTypes: list[list[int]], truckSize: int) -> int:
    l = sorted(boxTypes, key=itemgetter(1), reverse=True)
    sum = 0
    for i in range(0, len(l)):
        if truckSize == 0:
            break
        if truckSize >= l[i][0]:
            sum += l[i][0] * l[i][1]
            truckSize -= l[i][0]
        else:
            sum += truckSize * l[i][1]
            truckSize -= truckSize
    print(sum)


boxTypes = [[5, 10], [2, 5], [4, 7], [3, 9]]
truckSize = 10
# Output: 8
maximumUnits(boxTypes, truckSize)
