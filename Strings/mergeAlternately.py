def mergeAlternately(word1: str, word2: str) -> str:
    s = ''
    if len(word1) == len(word2):
        for i in range(0, len(word1)):
            s = s + word1[i] + word2[i]
    elif len(word2) > len(word1):
        l3 = word2[0:len(word1)]
        for i in range(0, len(word1)):
            s = s + word1[i] + l3[i]
        s = s + word2[len(word1):]
    else:
        l3 = word1[0:len(word2)]
        print(l3)
        for i in range(0, len(word2)):
            s = s + l3[i] + word2[i]
        s = s + word1[len(word2):]
    print(s)


word1 = "abcd"
word2 = "pq"
# Output: "apbqcr"
mergeAlternately(word1, word2)
