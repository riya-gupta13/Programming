from functools import reduce


def xorOperation(n: int, start: int) -> int:
    nums = [None] * n
    for i in range(0, n):
        nums[i] = start + 2 * i
    print(nums)
    print(reduce(lambda a,b:a^b,nums))
    # ans = nums[0]
    # for i in range(1, len(nums)):
    #     ans =ans ^ nums[i]
    # print(ans)



n = 5
start = 0
# Output: 8
xorOperation(n, start)
