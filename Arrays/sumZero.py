def sumZero(n: int) -> list[int]:
    x = 0
    arr = []
    if n % 2 != 0:
        arr.append(x)
        for i in range(1, n // 2+1):
            arr.append(x - i)
        for i in range(1, n // 2+1):
            arr.append(x + i)
        print(arr)
    else:
        for i in range(1, n // 2+1):
            arr.append(x - i)
        for i in range(1, n // 2+1):
            arr.append(x + i)
        print(arr)


n = 4
# Output: [-7,-1,1,3,4]
sumZero(n)
