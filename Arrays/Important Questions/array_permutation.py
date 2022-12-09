def buildArray(self, nums: list[int]) -> list[int]:
    n = len(nums)
    list = []
    for i in range(0, n):
        arr = nums[nums[i]]
        list.append(arr)
    print(list)
