def countElements(nums: list[int]) -> int:
    num = sorted(nums)
    mini = min(num)
    maxi = max(num)
    count = 0
    for i in num:
        if i != mini and i != maxi:
            count += 1
    return count


nums = [11, 1, 1, 1, 2, 2, 2, 3]
# Output: 2
print(countElements(nums))
