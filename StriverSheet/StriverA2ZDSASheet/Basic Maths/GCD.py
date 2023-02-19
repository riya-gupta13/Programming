def gcd(a, b):
    if b == 0:
        return a
    # euclidean's formula
    return gcd(b, a % b)
