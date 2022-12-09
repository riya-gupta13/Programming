def wordBreak(s: str, wordDict: list[str]) -> bool:
    w = "".join(wordDict)
    if w in s:
        print(True)
    else:
        print(False)


s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
# Output: true
wordBreak(s, wordDict)
