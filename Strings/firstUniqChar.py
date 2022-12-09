def firstUniqChar(s: str) -> int:
    l=list(s)
    print(l)
    for i in l:
        c=s.count(i)
        if c==1:
            print(s.index(i))
            return s.index(i)
    return -1


s =  "aabbc"
# Output: 0
print(firstUniqChar(s))