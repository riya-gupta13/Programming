# https://practice.geeksforgeeks.org/problems/minimum-characters-to-be-added-at-front-to-make-string-palindrome/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article
def minCharsforPalindrome(str):
    n = len(str)
    i = 0
    j = len(str) - 1
    lastIndex = len(str) - 1
    while i <= j:
        if str[i] == str[j]:
            i += 1
            j -= 1
        else:
            lastIndex -= 1
            j = lastIndex

    added=n-1-lastIndex
    return added

s = "tcitkg"
print(minCharsforPalindrome(s))
