from itertools import combinations


def minimumSum(num: int) -> int:
    l = list(str(num))
    li = sorted(l)
    print(li)
    sum1 = li[0]+ li[2]
    sum2 = li[1] + li[3]
    print(int(sum1) + int(sum2))


num = 4009
# Output: 52
minimumSum(num)
