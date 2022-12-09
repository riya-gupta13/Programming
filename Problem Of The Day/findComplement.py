def findComplement(num: int) -> int:
    binary = "{0:b}".format(int(num))
    l = list(binary)
    for i in range(0, len(l)):
        if l[i] == '1':
            l[i] = '0'
        else:
            l[i] = '1'
    print(l)
    decimal = int("".join(l), 2)
    res= int("".join(str(decimal)))
    print(res)
    return res

num = 5
# Output: 2
findComplement(num)
