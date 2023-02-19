def maxconsecutiveOne(s):
    ans = s.split('0')
    print(ans)
    return max(map(len, ans))


print(maxconsecutiveOne('11000111101010111'))
