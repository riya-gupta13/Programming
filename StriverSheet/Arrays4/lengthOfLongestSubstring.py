def lengthOfLongestSubstring(s: str) -> int:
    left = 0
    right = 0
    dict = {}
    length = 0
    while right < len(s):
        if s[right] in dict.keys():
            left = max(dict[s[right]] + 1, left)
        dict.__setitem__(s[right], right)
        length = max(length, right - left + 1)
        right += 1
    return length


s = "abcabcbb"
# Output: 3
print(lengthOfLongestSubstring(s))
