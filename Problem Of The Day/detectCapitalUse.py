def detectCapitalUse(word: str) -> bool:
    if word.islower():
        print(True)
    if word.istitle():
        print(True)
    if word.isupper():
        print(True)
    else:
        print(False)


word = "Flag"
# Output: true
detectCapitalUse(word)