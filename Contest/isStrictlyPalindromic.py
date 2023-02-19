def isStrictlyPalindromic(n: int) -> bool:
    ans = ''
    if n >= 1:
        isStrictlyPalindromic(n // 2)
    print(n % 2)
    ans += str(n % 2)
    print(ans)


n = 4
# Output: false
isStrictlyPalindromic(n)
