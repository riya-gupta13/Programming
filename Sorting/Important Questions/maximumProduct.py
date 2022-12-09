def maximumProduct(nums: list[int]) -> int:
    nums = sorted(nums)
    product = nums[-1] * nums[-2] * nums[-3]
    product2 = nums[0] * nums[1] * nums[-1]
    return max(product, product2)


nums = [1, 2, 3,5,6]
maximumProduct(nums)