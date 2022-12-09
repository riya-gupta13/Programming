def countWords(words1: list[str], words2: list[str]) -> int:
    count = 0
    for i in words2:
        for j in words2:
            if i == j:
                if words1.count(i) == words2.count(j) == 1:
                    print(i, j)
                    count += 1
    print(count)


words1 = ["b", "bb", "bbb"]
words2 = ["a", "a", "a", "ab"]
# Output: 2
countWords(words1, words2)
