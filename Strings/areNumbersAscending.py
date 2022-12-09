def areNumbersAscending(s: str) -> bool:
    new=s.split()
    print(new)
    l=[]
    for i in new:
        if i.isdigit():
            l.append(int(i))
    print(sorted(l),l)
    li=[]
    for i in range(0,len(l)-1):
        if l[i]<l[i+1]:
            li.append(True)
        else:
            li.append(False)
    print(li)
    if False in li:
        print(False)
    else:
        print(True)
    # if sorted(l)==l:
    #     print("True")
    # else:
    #     print("False")


s = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
# Output: true
areNumbersAscending(s)