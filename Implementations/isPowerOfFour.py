def isPowerOfFour(n: int) -> bool:
    count=0
    while n>4:
        if n%4==0:
            count+=1
        n=n//4
    count+=1
    if 4**count==n:
        print(True)
    else:
        print(False)

isPowerOfFour(4)