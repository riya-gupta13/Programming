def strStr(haystack: str, needle: str) -> int:
    ans = haystack.replace(needle, '#')
    if '#' in ans:
        return ans.index('#')
    else:
        return -1


haystack = "hello"
needle = "ll"
print(strStr(haystack, needle))
