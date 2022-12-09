def bitwiseComplement(n: int) -> int:
    b = bin(n).replace('0b', '')
    b = list(b)
    for i in range(0, len(b)):
        if b[i] == '0':
            b[i] = '1'
        else:
            b[i] = '0'
    print(b)
    decimal = int("".join(b), 2)
    res = int("".join(str(decimal)))
    print(res)

n = 10
# Output: 2
bitwiseComplement(n)
