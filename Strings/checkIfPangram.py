def checkIfPangram(sentence: str) -> bool:
    alphabets='abcdefghijklmnopqrstuvwxyz'
    if all(x in set(sentence) for x in alphabets):
        print("True")
    else:
        print("False")


sentence = "avcdiojhgfderthjklmnbv"
# Output: true
checkIfPangram(sentence)