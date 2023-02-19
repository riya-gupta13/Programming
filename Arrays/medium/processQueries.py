def processQueries(queries: list[int], m: int) -> list[int]:
    P = []
    for i in range(1, m + 1):
        P.append(i)
    print(P)
    res = []
    for i in queries:
        ind = P.index(i)
        res.append(ind)
        P.insert(0, P.pop(ind))
        print(P)
    print(res)


queries = [4,1,2,2]
m = 4
processQueries(queries, m)
# Output: [2,1,2,1]
