class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insertionSortListBest(self, head: ListNode):
    dummy = ListNode(0, head)
    prev = head
    cur = head.next
    while cur:
        if cur.val > prev.val:
            prev = cur
            cur = cur.next
        tmp = dummy
        while cur.val > tmp.next.val:
            tmp = tmp.next
        prev.next = cur.next
        cur.next = tmp.next
        tmp.next = cur
        cur = prev.next


def insertionSortList(self, head: ListNode):
    # will give TLE
    cur = head
    while cur:
        j = head
        while j != cur:
            if j.val > cur.val:
                j.val, cur.val = cur.val, j.val
            j = j.next
        cur = cur.next
    return head
