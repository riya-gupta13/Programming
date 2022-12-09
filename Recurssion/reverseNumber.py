sum = 0


def reverse(n):
    global sum
    if n <= 0:
        return ''
    sum = sum * 10 + n % 10
    # print(sum)
    reverse(n // 10)
    return sum


print(reverse(901))
