import math


def seive(n):
    arr = [1] * (n + 1)
    for i in range(2, int(math.sqrt(n))+1):
        if arr[i] != 0:
            for j in range(i*i, n+1, i):
                arr[j] = 0

    print(arr)
    for i in range(0,len(arr)):
        if arr[i] == 1:
            print(i)


seive(100)
