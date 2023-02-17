#     A
#   A B A
# A B C B A
# A B C D C B A

n = 5
for i in range(n):
    # space
    for j in range(1, n - i - 1):
        print(" ", end="")
    char = 65
    breakpoint = (2 * i + 1) // 2
    # char
    for j in range(1, 2 * i + 2):
        print(chr(char), end="")
        if j <= breakpoint:
            char += 1
        else:
            char -= 1
    # space
    for j in range(n - i - 1):
        print(" ", end="")
    print(" ")
