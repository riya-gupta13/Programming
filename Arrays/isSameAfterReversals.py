def isSameAfterReversals(num: int) -> bool:
    def reverse(n):
        rev = 0
        while n > 0:
            rev = rev * 10 + n % 10
            n = n // 10
        return rev

    rev = reverse(num)
    rev2 = reverse(rev)
    print(rev,rev2)
    if num == rev2:
        print("True")
    else:
        print("false")


num = 0
# Output: true
isSameAfterReversals(num)
