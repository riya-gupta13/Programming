import collections


class Solution:
    def maxSlidingWindow(nums: list[int], k: int):
        output = []
        q = collections.deque()
        l = r = 0
        while r < len(nums):
            while q and nums[q[-1]] <= nums[r]:
                q.pop()
            q.append(r)

            # remove left val from window
            if l > q[0]:
                q.popleft()
            #
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output
