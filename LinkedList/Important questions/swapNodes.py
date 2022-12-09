class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swapNodes(self, head: ListNode, k: int) -> ListNode:
    cur = head
    right = head
    # as 1 indexed so
    k -= 1
    # traversing to k-node from beginning
    while k:
        cur = cur.next
        k -= 1
    #  this left is the kth node from beginning
    left = cur
    # using the same approach to k-node from behind as we used in remove nth node
    secnd = cur.next
    while secnd:
        secnd = secnd.next
        right = right.next
    # then swapping
    # right will be the kth node from behind
    left.val, right.val = right.val, left.val
    return head
