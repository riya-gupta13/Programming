# 12345
# 1234
# 123
# 12
# 1

n = 6
for i in range(1, n + 1):
    for j in range(1, n - i + 1):
        print(j, end=" ")
    print(" ")
