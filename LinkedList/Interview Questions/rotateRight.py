import re


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def rotateRight(self, head: ListNode, k: int) -> ListNode:
    if not head:
        return head
    length, tail = 1, head
    while tail.next:
        tail = tail.next
        length += 1
    k = k % length
    if k == 0:
        return head
    else:
        cur = head
        for i in range(length - k - 1):
            cur = cur.next
        newHead = cur.next
        cur.next = None
        tail.next = head
        return newHead


