def toGoatLatin(sentence: str) -> str:
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    sentence = sentence.split()
    for s in range(0, len(sentence)):
        if sentence[s][0] in vowels:
            sentence[s] = sentence[s] + 'ma'
        else:
            sentence[s] = sentence[s][1:] + sentence[s][0] + 'ma'
        sentence[s] = sentence[s] + (s + 1) * 'a'
    print(" ".join(sentence))


sentence = "The quick brown fox jumped over the lazy dog"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
toGoatLatin(sentence)
