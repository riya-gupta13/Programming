def firstPalindrome(words: list[str]) -> str:
    # for i in range(0, len(words)):
    #     temp = ''
    #     char = ''
    #     for j in words[i]:
    #         print(j)
    #         char = j
    #         temp = char + temp
    #     if temp == words[i]:
    #         print(temp, words[i])
    #         return temp
    l=[]
    for i in words:
        if i == i[::-1]:
            # print(i)
            l.append(i)
    if len(l)==0:
        print('hi')
        return ''
    else:
        return l[0]


words = ["def","ghi"]
# Output: "ada"
firstPalindrome(words)
