def palindrome(n):
    reverse = 0
    m = n
    while n != 0:
        reverse = reverse * 10 + n % 10
        n = n // 10
    if reverse == m:
        print("True")
    else:
        print("False")


palindrome(121)
