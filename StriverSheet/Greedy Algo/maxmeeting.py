def maxMeeting(s, e, n):
    l = []
    for i in range(0, len(s)):
        l.append([s[i], e[i], i + 1])
    print(l)
    ans = []
    l.sort(key=lambda x: x[1])
    ans.append(l[0][2])
    endLimit = l[0][1]
    for i in range(0, len(l)):
        if l[i][0] > endLimit:
            ans.append(l[i][2])
            endLimit = l[i][1]
    for i in ans:
        print(i, end=" ")
    print(ans)


N = 6
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 5, 7, 9, 9]
print(maxMeeting(start, end, N))
# Output: 1 2 4 5
