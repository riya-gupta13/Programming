from operator import itemgetter


def sortByBits(arr: list[int]) -> list[int]:
    l = []
    for i in arr:
        l.append(bin(i)[2:])
    print(l)
    ar = []
    for i in l:
        if '1' in i:
            c = i.count('1')
            ar.append([int(i, 2), c])
        else:
            ar.append([int(i, 2), 0])
    s = sorted(ar)
    li = []
    for i in sorted(s):
        li.append(i[0])
    print(li)

    d = []
    for i in arr:
        x = len(bin(i).replace('0', '')) - 1
        d.append([x, i])
    s=sorted(d)
    for x in s:
        result = [x[1]]
        li.append(result)
    print(li)


arr = [0,1,2,3,4,5,6,7,8]
# Output: [1,2,4,8,16,32,64,128,256,512,1024],[0,1,2,4,8,3,5,6,7]
sortByBits(arr)
