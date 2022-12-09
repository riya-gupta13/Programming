def numberOfMatches(n: int) -> int:
    return n-1
    # match = 0
    # m=0
    # while n != 1:
    #     if n % 2 == 0:
    #         match = n // 2
    #         n = n - match
    #         print(match)
    #     else:
    #         match = (n - 1) // 2
    #         n = n - match
    #         print(match)
    #     m=m+match
    # print(m)


n = 3
# Output: 6
numberOfMatches(n)
