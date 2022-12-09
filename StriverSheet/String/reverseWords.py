def reverseWords(self, s: str) -> str:
    temp = ''
    s = s.strip()
    l = s.split(' ')
    for i in range(len(l) - 1, -1, -1):
        if l[i] != '':
            temp += l[i] + " "
    return temp.strip()