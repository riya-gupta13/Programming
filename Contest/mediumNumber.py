def mediumNumber():
    tests = int(input(""))
    while tests:
        a = int(input(""))
        b = int(input(""))
        c = int(input(""))
        arr = [a, b, c]
        arr = sorted(arr)
        print(arr[1])
        tests -= 1

mediumNumber()
