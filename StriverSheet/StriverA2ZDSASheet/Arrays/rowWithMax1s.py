# https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=row-with-max-1s


def rowWithMax1s(arr, n, m):
    maxi = 0
    ans = -1
    for i in range(n):
        r = arr[i].count(1)
        if r > maxi:
            maxi = max(r, maxi)
            ans = i
    return ans


n = 4
m = 4
arr = [[0, 1, 1, 1],
       [0, 0, 1, 1],
       [1, 1, 1, 0],
       [0, 0, 0, 0]]
# Output: 2
print(rowWithMax1s(arr, n, m))
