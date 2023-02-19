list = [7, 2, 9, 3, 5]
l2 = [2, 2, 2, 3, 4]
# s = set(l2)
ar = sorted(l2)
print(ar)
for i in range(0, len(ar) - 1):
    if ar[i] == ar[i + 1]:
        i+=1
    else:
        if i == len(ar[i - 1:]):
            print(i)
