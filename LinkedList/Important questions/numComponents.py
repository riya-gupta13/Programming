class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def numComponents(self, head: ListNode, nums: list[int]) -> int:
        nums = set(nums)
        count = 0
        connected = False

        cur = head
        while cur:
            if cur.val in nums and not connected:
                connected = True
                count += 1
            elif cur.val not in nums and connected:
                connected = False
            cur = cur.next
        return count
