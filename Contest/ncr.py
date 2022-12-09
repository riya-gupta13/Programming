# n//(n-r)(r)
# n = int(input(""))
# r = int(input(""))

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

def combination(n, r):
    nfact = factorial(n)
    fact1 = factorial(n - r)
    fact2 = factorial(r)
    value = nfact // (fact1 * fact2)
    print(value)


combination(5, 2)

#         *
#        ***
#       *****
#      *******
#     *********
#    ***********
#   *************
#  ***************
# *****************
n = 10
for i in range(1, n):
    temp = i
    for j in range(1, n - i):
        print(" ", end="")
    for k in range(0, (2 * i) - 1):
        print("*", end="")
    for m in range(1, n - i):
        print(" ", end="")
    print(" ")
