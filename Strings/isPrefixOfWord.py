def isPrefixOfWord(sentence: str, searchWord: str) -> int:
    l = []
    sentence = sentence.split()
    for i in range(0, len(sentence)):
        j = sentence[i][:len(searchWord)]
        if j.__contains__(searchWord):
            l.append(i + 1)
    if len(l) == 0:
        print("-1")
    for j in l:
        if len(l) == 1:
            print(j)
        elif len(l) > 1:
            print(j)
            break


sentence = "this problem is an easy problem"
searchWord = "pro"
# Output: 4
isPrefixOfWord(sentence, searchWord)
