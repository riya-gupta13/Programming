def minStartValue(nums: list[int]) -> int:
    i = 1
    while True:
        switch = True
        summ = i
        for j in nums:
            summ += j
            if summ < 1:
                switch = False
                break
        if switch:
            return i
        i += 1


nums = [1, 2]
# Output: 5
minStartValue(nums)
