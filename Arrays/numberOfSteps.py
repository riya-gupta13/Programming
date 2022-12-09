def numberOfSteps(num: int) -> int:
    count = 0
    while num != 0:
        if num % 2 == 0:
            num = num // 2
            count = count + 1
            print(num)
        else:
            num = num - 1
            count = count + 1
            print(num)
    print("Count", count)


num = 123
# Output: 6
numberOfSteps(num)
