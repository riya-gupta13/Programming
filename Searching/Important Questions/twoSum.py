def twoSum(numbers: list[int], target: int):
    l = 0
    h = len(numbers) - 1

    while l < h:
        sum = numbers[l] + numbers[h]
        if sum < target:
            l += 1
        elif sum > target:
            h -= 1
        else:
            return [l + 1, h + 1]


numbers = [2, 3, 4]
target = 6
print(twoSum(numbers, target))
