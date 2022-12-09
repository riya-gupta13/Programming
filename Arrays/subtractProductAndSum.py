def subtractProductAndSum(n: int) -> int:
    l = list(str(n))
    print(l)
    product = 1
    sum = 0
    for i in l:
        product = product * int(i)
        sum = sum + int(i)
    print(product, sum)
    result = product - sum
    print(result)


n = 4421
# Output: 15
subtractProductAndSum(n)
