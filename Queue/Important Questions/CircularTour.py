# https://practice.geeksforgeeks.org/problems/circular-tour/1
def tour(lis, n):
    start = 0
    extraFuel = 0
    reqFuel = 0
    for i in range(n):
        extraFuel += lis[i][0] - lis[i][1]
        if extraFuel < 0:
            start = i + 1
            reqFuel += extraFuel
            extraFuel = 0
    if reqFuel + extraFuel >= 0:
        return start
    else:
        return -1
