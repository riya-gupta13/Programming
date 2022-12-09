class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head
        odd = head
        evenHead = head.next
        even = head.next
        cur = head
        count = 1
        while cur:
            if count > 2 and count % 2 != 0:
                odd.next = cur
                odd = odd.next
            elif count > 2 and count % 2 == 0:
                even.next = cur
                even = even.next
            cur = cur.next
            count += 1
        even.next = None
        odd.next = evenHead
        return head
