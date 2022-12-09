class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
    dummy = ListNode(0, head)
    # reach node at position left
    leftPrev = dummy
    cur = head
    for i in range(left - 1):
        leftPrev = cur
        cur = cur.next
    # now cur=left and leftPrev node is before left
    # now reverse from left to rght
    prev = None
    for i in range(right - left + 1):
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt
    # update pointers
    leftPrev.next.next = cur  # cur node is after right
    leftPrev.next = prev  # prev is right
    return dummy.next
