# odd numbers list btwn 20-80

start = 20
end = 80
# odd=lambda i: i%2!=0
# l = [if i%2!=0: for i in range(start, end + 1) ]
odd_num = [i for i in range(start, end + 1) if i % 2 != 0]
odd_num.remove(53)
print(odd_num)

for i in range(len(odd_num) - 1):
    if odd_num[i + 1] - odd_num[i] != 2:
        print(odd_num[i] + 2)
        break
else:
    print(-1)


def fibonacci(n):
    fiblist = [0, 1]
    while len(fiblist) < n:
        fiblist.append(fiblist[-1] + fiblist[-2])
    return fiblist


print(fibonacci(12))
