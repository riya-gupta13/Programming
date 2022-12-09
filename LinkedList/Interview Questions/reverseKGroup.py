class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroups(self, head: ListNode, k: int, l) -> ListNode:
        def length(head):
            len = 0
            cur = head
            while cur:
                cur = cur.next
                len += 1
            return len

        l = length(head)
        if l < k:
            return head
        cur = head
        prev = None
        count = 0
        nxt = None
        while cur and count < k:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            count += 1

        if nxt is not None:
            head.next = self.reverseKGroups(nxt, k, l - k)

        return prev
