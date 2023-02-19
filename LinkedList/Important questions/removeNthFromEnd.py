class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    # approach
    # frst traverse from begining to the kth node
    # then take another pointer and move from head till rght reaches end
    # once right bcmes null left will be at the node before whch we wnt to delete
    dummy = ListNode(0, head)
    left = dummy
    right = head
    while n > 0 and right:
        right = right.next
        n -= 1
    while right:
        left = left.next
        right = right.next
    left.next = left.next.next
    return dummy.next
