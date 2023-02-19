def isSumEqual(firstWord: str, secondWord: str, targetWord: str) -> bool:
    alpha = 'abcdefghij'

    def getIndex(word):
        s = ''
        for i in range(0, len(word)):
            index = alpha.index(word[i])
            s += str(index)
        return int(s)

    firstIndex = getIndex(firstWord)
    secondIndex = getIndex(secondWord)
    target = getIndex(targetWord)
    print(firstIndex,secondIndex,target)
    if firstIndex + secondIndex == target:
        print("True")
    else:
        print("False")


firstWord = "aaaj"
secondWord = "a"
targetWord = "aaaa"
# Output: true
isSumEqual(firstWord, secondWord, targetWord)
