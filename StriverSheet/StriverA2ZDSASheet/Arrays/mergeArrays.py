# https://practice.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=union-of-two-sorted-arrays


def mergeArrays(a, b, n, m):
    d = {}
    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in b:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    print(sorted(list(d.keys())))
    return sorted(list(d.keys()))



n = 5
a = [2, 2, 3, 4, 5]
m = 5
b = [1, 1, 2, 3, 4]
mergeArrays(a, b, n, m)
