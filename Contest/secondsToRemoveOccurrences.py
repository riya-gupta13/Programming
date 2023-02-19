def secondsToRemoveOccurrences(s: str) -> int:
    flag=False
    while flag:
        if '01' in s:
            s = s.replace('01','10')
            


s = "0110101"
# Output: 0
secondsToRemoveOccurrences(s)
