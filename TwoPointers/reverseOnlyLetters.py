def reverseOnlyLetters(s: str):
    alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    res = []
    for i in s:
        if i in alphabets:
            res.append(i)
    print(res)
    j = len(res) - 1
    a = ''
    for i in range(0, len(s)):
        if s[i] in alphabets:
            a += res[j]
            j -= 1
        else:
            a += s[i]
    print(a)




s = "OS@kDN"
reverseOnlyLetters(s)
