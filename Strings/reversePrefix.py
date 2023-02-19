def reversePrefix(word: str, ch: str) -> str:
    if ch in word:
        index = word.index(ch)
        print(index)
        print(word[0:index + 1][::-1]+ word[index+1:])
        return word[0:index + 1][::-1] + word[index+1:]
    else:
        print(word)
        return word
    # for i in range(len(s)-1,-1,-1):
    #     temp=''
    #     char=s[i]
    #     temp=char+temp
    #     st=st+temp
    # print(st)


word = "arzquwnjyn"
ch = "j"
# Output: "dcbaefd"
reversePrefix(word, ch)
