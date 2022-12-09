class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode):
    left = None
    right = None
    dummy = ListNode(0, list1)
    cur = list1
    index = 0
    while cur:
        if index == a - 1:
            left = cur
        elif index == b + 1:
            right = cur
        cur = cur.next
        index += 1
    left.next = list2
    tmp = list2
    while tmp.next:
        tmp = tmp.next
    tmp.next = right
    return dummy.next
