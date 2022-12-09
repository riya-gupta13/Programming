def sumOddLengthSubarrays(arr: list[int]) -> int:
    l = []
    for x in range(1, len(arr) + 1, 2):
        i = x
        j = 0
        while j <= len(arr) and i <= len(arr):
            l.append(sum(arr[j:i]))
            j += 1
            i += 1
    print(sum(l))
    return sum(l)


arr = [1, 2, 3]
sumOddLengthSubarrays(arr)
