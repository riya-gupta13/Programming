def shuffle(nums: list[int], n: int) -> list[int]:
    mid = len(nums) // 2
    new_ar = []
    pointer = 0
    for i in range(0, mid):
        new_ar.insert(pointer, nums[i])
        new_ar.insert(pointer + 1, nums[i + mid])
        pointer = pointer + 2
    print(new_ar)
    return new_ar


nums = [1, 2, 3, 4, 4, 3, 2, 1]
n = 3
shuffle(nums, n)
