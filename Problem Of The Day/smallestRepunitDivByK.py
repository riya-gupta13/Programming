def smallestRepunitDivByK(k: int) -> int:
    count = 0
    length = 1
    for i in range(length, k + 1):
        count = (count * 10 + 1) % k
        if count == 0:
            # print(i)
            return i
    return -1


k = 5
# Output: 1
print(smallestRepunitDivByK(k))
