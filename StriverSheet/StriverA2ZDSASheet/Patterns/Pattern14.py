# A
# A B
# A B C
# A B C D
# A B C D E

for i in range (65,70):
    # inner loop
    for j in range(65,i+1):
        print(chr(j),end="")
    print()