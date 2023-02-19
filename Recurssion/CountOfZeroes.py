count=0
def countZeroes(n):
    global count
    if n <= 0:
        return count
    rem = n % 10
    if 0 == rem:
        count += 1
    countZeroes(n // 10)
    return count


print(countZeroes(4500))
