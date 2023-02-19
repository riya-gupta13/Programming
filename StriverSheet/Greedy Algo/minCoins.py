def findMin(V):
    deno = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
    n = len(deno)
    ans = []
    for i in range(n - 1, -1, -1):
        while V >= deno[i]:
            V -= deno[i]
            ans.append(deno[i])
    print(len(ans))
    for i in ans:
        print(i)


V = 70
findMin(V)
