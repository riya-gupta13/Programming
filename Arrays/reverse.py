def reverse(x: int) -> int:
    res=0
    rev = 0
    y = abs(x)
    while y > 0:
        rev = rev * 10 + y % 10
        y = y // 10
    if pow(-2,31)<=rev<=(pow(2,31)-1):
        if x < 0:
            res = -rev
            print(res)
            return res
        else:
            res = rev
            print(res)
            return res
    else:
        print('0')
        return 0



x = -123
# Output: -321
reverse(x)
