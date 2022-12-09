def numOfStrings(patterns: list[str], word: str) -> int:
    count = 0
    for i in patterns:
        if word.__contains__(i):
            count = count + 1
    print(count)


patterns = ["a","abc","bc","d"]
word = "abc"
# Output: 2
numOfStrings(patterns, word)
