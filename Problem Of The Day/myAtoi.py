def myAtoi(s: str) -> int:
    s = s.strip()
    # print(s)
    num = ''
    l = ''
    for i in range(0, len(s)):
        if s[0].isalpha():
            return 0
        if s.__contains__('.'):
            ind=s.index('.')
            l=s[:ind]
            print(l)
            break
        if s[i].startswith('+'):
            if s[i][1:].lstrip('+').isdigit():
                l += s[i]
        # if s[i].startswith('-'):
        if s.__contains__('-'):
            if s[i].lstrip('-').isdigit():
                num += s[i]
                print(num)
                l = '-' + num
        else:
            if s[i].isdigit():
                l += s[i]
    print(l)
    # -231, 231 - 1
    if pow(-2, 31) < int(l) < (pow(2, 31) - 1):
        print(int(l))
    if int(l) > 2 ** 31 - 1:
        l = 2 ** 31 - 1
    elif int(l) < -1 * (2 ** 31):
        l = -1 * (2 ** 31)
    print(int(l))

s =  "3.44"
# Output: 4193
myAtoi(s)
