# x = 10
# l = [1, 2, 3]


def outer():
    x = 11
    l = [1, 2, 3]
    inner(x, l)
    print("outer",x, l)


def inner(y, li):
    y = 12
    li.append(5)
    print("inner",y, li)

outer()
#
#
# # func()
# # print(x)
import math

# n=0-10^9
# prime number
n = 7
# math.sqrt(n)
count = 0


#
# def primeCheck(n):
#     s = 1
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             s = 0
#             print("not prime")
#             break
#         else:
#             continue
#     if s == 1:
#         print("prime")
#     return s
#
#
# print(primeCheck(1))
# Given a non-negative integer x, return the square root of x rounded down to the nearest integer.
# The returned integer should be non-negative as well.
# 16--2*2*2*2
# 8-2*2*2
def findSquareRoot(x):
    for i in range(0, x / 2):
        if i * i == x:
            return i
        else:
            if i * i > x:
                return i - 1


def binarySearch(x):
    low = 0
    high = x
    while low <= high:
        mid = low + high // 2
        if mid * mid <= x < (mid + 1) * (mid + 1):
            return mid
        elif mid * mid < x:
            low = mid + 1
        else:
            high = mid - 1
        print(mid)
    return low


print(binarySearch(2))
