class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        prev = dummy
        cur = head
        while cur and cur.next:
            # save ptrs
            nxtPair = cur.next.next
            secnd = cur.next
            # swap
            cur.next = nxtPair
            secnd.next = cur
            prev.next = secnd
            # update ptrs
            prev = cur
            cur = nxtPair
        return dummy.next
