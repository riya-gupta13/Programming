class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def isPalindrome(self, head: [ListNode]) -> bool:
    nums = []
    cur = head
    while cur:
        nums.append(cur.val)
        cur = cur.next

    left = 0
    right = len(nums) - 1
    while left <= right:
        if nums[left] != nums[right]:
            return False
        left += 1
        right -= 1
    return True
