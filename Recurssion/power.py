def power(base, exp):
    if exp < 0:
        print("exp can't be a negative number")
    if exp == 0:
        return 1
    if exp == 1:
        return base
    else:
        return base * power(base, exp - 1)


print(power(2, 3))
