# https://leetcode.com/problems/find-the-most-competitive-subsequence/
def mostCompetitive(nums: list[int], k: int):
    attempts = len(nums) - k
    stack = []
    for num in nums:
        while stack and num < stack[-1] and attempts > 0:
            stack.pop()
            attempts -= 1
        stack.append(num)

    return stack[:k]


nums = [71, 18, 52, 29, 55, 73, 24, 42, 66, 8, 80, 2]
k = 3
print(mostCompetitive(nums, k))
