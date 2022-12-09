p = 0


def Palindrome(n):
    global p
    if n <= 0:
        return ''
    p = p * 10 + n % 10
    # print(p)
    Palindrome(n // 10)
    if p == n:
        return True
    else:
        return False


print(Palindrome(121))
