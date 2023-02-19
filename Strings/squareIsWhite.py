def squareIsWhite(coordinates: str) -> bool:
    alphabets = 'Aabcdefghijklmnopqrstuvwxyz'
    d = {'oddodd': 'black', 'eveneven': 'black', 'evenodd': 'white', 'oddeven': 'white'}
    l = list(coordinates)
    for i in range(0, len(l)):
        if l[i] in alphabets:
            index = alphabets.index(l[i])
            l[i] = str(index)
    print(l)
    n = ''
    for i in range(0, len(l)):
        if int(l[i]) % 2 == 0:
            print("even")
            n = n + 'even'
        else:
            print("odd")
            n = n + 'odd'
    print(n)
    print(d[n])
    if d[n] == 'black':
        print("False")
        return False
    else:
        print("True")
        return True


coordinates = "h4"
# Output: false
# oddodd/evenevn-blck
# evebodd/oddeven-white
squareIsWhite(coordinates)
