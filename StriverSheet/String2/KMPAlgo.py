# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/
def strStr(self, haystack: str, needle: str) -> int:
    if needle == "":
        return 0
    # to find lps
    lps = [0] * len(needle)
    prevLPS = 0
    i = 1
    while i < len(needle):
        if haystack[i] == needle[i]:
            lps[i] += 1
            prevLPS += 1
            i += 1
        elif prevLPS == 0:
            lps[i] = 0
            i += 1
        else:
            prevLPS = lps[prevLPS - 1]

    i = 0  # for haystack
    j = 0  # for needle
    while i < len(haystack):
        if haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            if j == 0:
                i += 1
            else:
                j = lps[j - 1]
        if j == len(needle):
            return i - len(needle)
    return -1
