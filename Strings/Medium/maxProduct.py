def maxProduct(words: list[str]) -> int:
    n = len(words)
    char_set = [set(words[i]) for i in range(n)]  # precompute hashset for each word
    print(char_set)
    max_val = 0
    for i in range(0, len(words)):
        for j in range(i + 1, len(words)):
            if not (char_set[i] & char_set[j]):
                max_val = max(max_val, len(words[i]) * len(words[j]))


words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
# Output: 16
maxProduct(words)
