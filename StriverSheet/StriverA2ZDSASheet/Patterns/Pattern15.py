# A B C D E
# A B C D
# A B C
# A B
# A

n=6
for i in range(1,n+1):
    for j in range(65,65+(n-i-1)+1):
        print(chr(j),end=" ")
    print(" ")
