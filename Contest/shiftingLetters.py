def shiftingLetters(s: str, shifts: list[list[int]]) -> str:
    alpha = 'zabcdefghijklmnopqrstuvwxyza'
    new=s
    for i in shifts:
        str1 = new[i[0]:i[1]+1]
        print(str1)
        letter = ''
        for j in str1:
            if i[2] == 0:
                # print("J",alpha[alpha.index(j)-1])
                letter += alpha[alpha.index(j) - 1]
                # print("letters",letter)
            else:
                letter += alpha[alpha.index(j) + 1]
                # s = s.replace(str1, letter)
            # print("l",letter)
        s = s.replace(str1, letter)
        print("S", s)
    print(s)


s = "abc"
shifts = [[0, 1, 0], [1, 2, 1], [0, 2, 1]]
# Output: "ace"
shiftingLetters(s, shifts)
