class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeElements(head: [ListNode], val: int) -> [ListNode]:
    dummy = ListNode(next=head)
    prev, curr = dummy, head
    while curr:
        nxt = curr.next
        if curr.val == val:
            prev.next = nxt
        else:
            prev = curr
        curr = nxt
        return dummy.next


head = [1, 2, 6, 3, 4, 5, 6]
val = 6
# h=ListNode(head)
# removeElements(head, val)
