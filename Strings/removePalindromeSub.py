def removePalindromeSub(s: str) -> int:
    if not s:
        return 0
    if s == s[::-1]:
        return 1
    else:
        return 2


s = "baabb"
# Output: 1
removePalindromeSub(s)
