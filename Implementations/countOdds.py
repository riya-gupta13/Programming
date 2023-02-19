def countOdds(low: int, high: int) -> int:
    count = 0
    if low % 2 != 0:
        low -= 1
    count = (high + 1) - low
    print(count)


low = 8
high = 10

countOdds(low, high)
