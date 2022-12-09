def longestPalindrome(self, s: str) -> str:
    # approach-- we will be searching from centre and then moving left and rght cmpring if they are equal
    # but in this we can miss the even length palindrome's thats another edge cases
    # so for that we be string left and rght pointers from diff position
    res = 0
    resLen = 0
    for i in range(len(s)):
        # odd length
        l = i
        r = i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l:r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1

        # even length
        l = i
        r = i + 1  # here we are staring r from next pointer
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > resLen:
                res = s[l:r + 1]
                resLen = r - l + 1
            l -= 1
            r += 1
    return res
