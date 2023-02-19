def buildArray(target: list[int], n: int) -> list[str]:
    last=target[-1]
    l=[]
    for i in range(1,last+1):
        print(i)
        if i in target:
            l.append("Push")
        else:
            l.append("Push")
            l.append("Pop")
    print(l)


target = [1,2]
n = 3
# Output: ["Push","Push","Pop","Push"]
buildArray(target,n)
