def maximum69Number(num: int) -> int:
    number = str(num)
    n= number.replace('6','9',1)
    print(n)
    new=[]
    l=list(number)
    new.append(l)
    for i in range(0,len(l)):
        if l[i]=='6':
            l[i]='9'
            new.append(l)
            break
    print(new)
    l = list(number)
    for i in range(len(l)-1,-1,-1):
        if l[i] == '6':
            l[i] = '9'
            new.append(l)
            break
    print(new)
    print("".join(max(new)))

num = 9996
# Output: 9969
maximum69Number(num)
