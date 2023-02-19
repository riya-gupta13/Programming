class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def partition(self, head: [ListNode], x: int) -> [ListNode]:
    # approach tjke 2 list left rght, left will hve all less than x and rght all greater tahn x
    # then left's last will point head of rght anf rghts next pointgs to null

    left = ListNode()
    right = ListNode()
    lTail = left
    rTail = right
    while head:
        if head.val < x:
            lTail.next = head
            lTail = lTail.next
        else:
            rTail.next = head
            rTail = rTail.next
        head = head.next
    lTail.next = right
    rTail.next = None
    return left.next
