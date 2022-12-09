def partitionString(s: str) -> int:
    l=[]
    for i in range(0, len(s)+1):
        for j in range(i):
            l.append(s[j:i])
    print(l)
    # for i in l:
    #     if set(i)

s = "ssssss"
# Output: 4
partitionString(s)