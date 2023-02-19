class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteMiddle(self, head: ListNode) -> ListNode:
    slow = head
    fast = head
    prev=None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    if prev is None:
        return None
    prev.next = slow.next
    return head
