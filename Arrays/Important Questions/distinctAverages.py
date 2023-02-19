def distinctAverages(nums: list[int]) -> int:
    averages = []
    while nums:
        maximum = max(nums)
        minimum = min(nums)
        avg = (minimum + maximum) / 2
        averages.append(avg)
        nums.pop(nums.index(maximum))
        nums.pop(nums.index(minimum))
    return len(set(averages))


nums = [1,100]
distinctAverages(nums)
