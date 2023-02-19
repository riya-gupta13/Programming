def destCity(paths: list[list[str]]) -> str:
    l = []
    li = []
    for i in paths:
        l.append(i[0])
        li.append(i[1])
    d = dict(zip(l, li))
    print(d)
    for i in d.keys():
        for j in d.keys():
            if i == d[j]:
                print(i + "---" + d[j])
                l.remove(i)
                li.remove(i)
    print(l,li)
    print("".join(li))
    return "".join(li)



paths = [["A","Z"]]
# Output: "Sao Paulo"
destCity(paths)
