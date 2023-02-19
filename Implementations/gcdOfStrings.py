def gcdOfStrings(str1: str, str2: str) -> str:
    d = {}
    if len(str1) <= len(str2):
        s = str1
        st=str2
    else:
        s = str2
        st=str1
    ans=""
    for i in s:
        if i in st:
            ans+=i
        else:
            break
    print(ans)



str1 = "ABCABC"
str2 = "ABC"
gcdOfStrings(str1, str2)
