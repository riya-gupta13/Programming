def reverseWords(s: str) -> str:
    temp = ''
    s = s.strip()
    l = s.split(' ')
    print(l)
    for i in range(len(l) - 1, -1, -1):
        if l[i] != '':
            temp += l[i] + " "
    return (temp.strip())


s = "the sky is blue"
# Output: "blue is sky the"
print(reverseWords(s))
