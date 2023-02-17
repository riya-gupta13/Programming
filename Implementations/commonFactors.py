def commonFactors(a: int, b: int) -> int:
    ans = []
    count = 0
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            ans.append(i)
            count += 1
    print(ans)
    return count


a = 25
b = 30
commonFactors(a, b)
