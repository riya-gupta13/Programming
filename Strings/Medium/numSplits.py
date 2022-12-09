def numSplits(s: str):
    count = 0
    for i in range(0, len(s)):
        tempL = s[:i + 1]
        tempR = s[i + 1:]
        print(tempL, tempR)
        if len(set(tempL)) == len(set(tempR)):
            print("Matched", tempL, tempR)
            count += 1
    print(count)


s = "abcd"
# Output: 2
numSplits(s)
