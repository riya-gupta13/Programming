def validPalindrome(s: str) -> bool:
    # we are chceking from left amnf rght pointers if they are equal move forwrd
    # if they are not thy we try to remove from frnt skipL and chk
    # if not we try tp remove from rght and chk, it will return false if not otherwise true
    l = 0
    r = len(s) - 1
    while l <= r:
        if s[l] != s[r]:
            skipL = s[l + 1:r + 1]
            skipR = s[l:r]
            return (skipL == skipL[::-1] or skipR == skipR[::-1])
        l = l + 1
        r = r - 1
    return True
