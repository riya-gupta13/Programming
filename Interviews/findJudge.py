# turing test
def findJudge(N, trust):
    result = None
    setA = []
    setB = []
    for i in trust:
        setA.append(i[0])
        setB.append(i[1])
    print(set(setB), set(setA))
    for i in set(setB):
        if i not in set(setA):
            result = i
            break
        else:
            result = -1
    print(result)
    return result


N = 3
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]
findJudge(N, trust)
