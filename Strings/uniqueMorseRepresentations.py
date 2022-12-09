def uniqueMorseRepresentations(words: list[str]) -> int:
    morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
             ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    l = []
    for i in words:
        res = ''
        for j in i:
            index = alpha.index(j)
            res = res + morse[index]
        l.append(res)
    count=len(set(l))
    return count


words = ["gin","zen","gig","msg"]
# Output: 2
uniqueMorseRepresentations(words)
