def uniqueOccurrences(arr: list[int]) -> bool:
    d = {}
    for i in arr:
        d[i] = arr.count(i)
    print(d)
    print(d.values())
    print(set(d.values()))
    if len(d.values()) == len(set(d.values())):
        print(True)
    else:
        print(False)


arr = [-3,0,1,-3,1,1,1,-3,10,0]
# Output: true
uniqueOccurrences(arr)
