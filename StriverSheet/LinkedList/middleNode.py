class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next
        if not count % 2 == 0:
            mid = count // 2
            cur = head
            for i in range(mid):
                cur = cur.next
            return cur
        if count % 2 == 0:
            mid = count // 2
            cur = head
            for i in range(mid):
                cur = cur.next
            return cur
