def countVowelSubstrings(word: str) -> int:
    count = 0
    for i in range(len(word)+1):
        for j in range(i):
            # print(word[j:i])
            if set(word[j:i]) == set('aeiou'):
                count += 1
    print(count)


word = "cuaieuouac"
# Output: 2
countVowelSubstrings(word)
