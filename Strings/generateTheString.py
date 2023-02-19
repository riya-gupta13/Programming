def generateTheString(n: int) -> str:
    s=['a','b']
    if n%2==0:
        st=s[0]*(n-1)+s[1]*1
    else:
        st=s[0]*n
    print(st)


n = 7
# Output: "pppz"
generateTheString(n)