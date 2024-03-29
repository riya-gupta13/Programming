class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle(self, head: [ListNode]) -> [ListNode]:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    else:
        return None
    pointer = head
    while pointer != fast:
        pointer = pointer.next
        fast = fast.next
    return pointer

