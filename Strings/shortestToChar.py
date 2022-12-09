def shortestToChar(s: str, c: str) -> list[int]:
    global max
    l = list(s)
    indices = []
    for i in range(0, len(l)):
        if c == l[i]:
            indices.append(i)
    print(indices)
    ans = []
    for i in range(0, len(l)):
        max = 9999
        for j in indices:
            # print(l[i], abs(i-j))
            if abs(i - j) < max:
                max = abs(i - j)
            # print(abs(i-j),end=",")
        ans.append(max)
    print(ans)


s = "aaab"
c = "b"
# Output: [3,2,1,0,1,0,0,1,2,2,1,0]
shortestToChar(s, c)
