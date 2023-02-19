def divisors(n):
    ans = []
    for i in range(1, n):
        if n % i == 0:
            ans.append(i)
            if i != n / i:
                ans.append(n // i)
    print(ans)


divisors(36)
