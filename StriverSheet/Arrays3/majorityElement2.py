from math import floor


def majorityElement(nums: list[int]) -> list[int]:
    num1 = float('-inf')
    num2 = float('-inf')
    c1 = 0
    c2 = 0
    for i in nums:
        if num1 == i:
            c1 += 1
        elif num2 == i:
            c2 += 1
        elif c1 == 0:
            num1 = i
            c1 = 1
        elif c2 == 0:
            num2 = i
            c2 = 1
        else:
            c1 -= 1
            c2 -= 1
    c1 = 0
    c2 = 0
    ans = []
    for i in nums:
        if i == num1:
            c1 += 1
        if i == num2:
            c2 += 1
    if c1 > floor(len(nums) / 3):
        ans.append(num1)
    if c2 > floor(len(nums) / 3):
        ans.append(num2)
    return ans


nums = [-1, -1, -1]
Output: [3]
print(majorityElement(nums))
