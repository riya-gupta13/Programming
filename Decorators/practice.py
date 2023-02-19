def multiply_dec(func):
    def inner(i):
        return func(i)
    return inner

@multiply_dec
def multiply(n):
    return 5*n

print(multiply(4))