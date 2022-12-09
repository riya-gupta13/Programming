def decimalToBinary(n):
    # if n == 0:
    #     return 0
    # else:
    #     return n % 2 + 10 * decimalToBinary(n // 2)
    l = []
    while n != 0:
        rem = n % 2
        n = n // 2
        l.append(rem)
    # print("".join(str(l)))
    s = ''
    for i in l[::-1]:
        s += str(i)
    print(int(s))


print(decimalToBinary(13))
