def mostWordsFound(sentences: list[str]) -> int:
    l=[]
    for i in sentences:
        sentence=i.split(" ")
        l.append(len(sentence))
    print(max(l))


sentences = ["please wait", "continue to fight", "continue to win"]
# Output: 6
mostWordsFound(sentences)