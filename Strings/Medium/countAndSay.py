import collections
import json


def countAndSay(n: int) -> str:
    def helper(num):
        n = len(num)
        i = 0
        ans = ''
        while i < n:
            count = 1
            j = i
            while j < n - 1 and num[j] == num[j + 1]:
                count += 1
                j += 1
            ans += str(count) + num[i]
            i = j + 1
        return ans

    def solve(n):
        if n == 1:
            return '1'
        return helper(solve(n - 1))

    return solve(n)
    # if n == 1:
    #     return "1"
    # else:
    #     s = ''
    #
    #     temp = '1'
    #     for i in range(1, n):
    #         d = collections.Counter(str(temp))
    #         # print(d)
    #         for j in d.keys():
    #             val = d[j]
    #             key = j
    #             s += str(val)
    #             s += str(key)
    #         # print(s)
    #         temp = s
    #         s = ''
    #     return temp


n = 5
# Output: "1"
print(countAndSay(n))
