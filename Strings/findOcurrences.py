def findOcurrences(text: str, first: str, second: str) -> list[str]:
    text = text.split()
    print(text)
    l = []
    for i in range(0, len(text)-2):
        if first == text[i]:
            j = i
            if second == text[j + 1]:
                print(text[j + 2])
                l.append(text[j + 2])
    print(l)

# "jkypmsxd jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa kcyxdfnoa jkypmsxd kcyxdfnoa"
# "kcyxdfnoa"
# "jkypmsxd"
text = "jkypmsxd jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa kcyxdfnoa jkypmsxd kcyxdfnoa"
first = "kcyxdfnoa"
second = "jkypmsxd"
findOcurrences(text, first, second)
