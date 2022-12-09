def replaceDigits(s: str) -> str:
    l=list(s)
    alpha='abcdefghijklmnopqrstuvwxyz'
    for i in range(1,len(l),2):
        a = alpha.index(l[i - 1])
        index = a + int(l[i])
        val = alpha[index]
        l[i]=val
    print("".join(l))



s = "a1b2c3d4e"
# Output: "abbdcfdhe"
replaceDigits(s)