def isPalindrome(strng):
    if len(strng) == 0:
        return True
    if strng[0] != strng[len(strng) - 1]:
        return False
    print(strng[1:-1])
    return isPalindrome(strng[1:-1])


isPalindrome("amma")
