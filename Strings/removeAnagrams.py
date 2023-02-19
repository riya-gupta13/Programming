def removeAnagrams(words: list[str]) -> list[str]:
    wordss = words.copy()
    for i in range(0, len(words)-1):
        # print(sorted(words[i]),sorted(words[j]))
        # print(i,i+1)
        if sorted(words[i]) == sorted(words[i+1]):
            wordss.remove(words[i+1])
            # w.append(words[i+1])
    print(wordss)


words =["a","b","a"]
# Output: ["abba","cd"]
removeAnagrams(words)
