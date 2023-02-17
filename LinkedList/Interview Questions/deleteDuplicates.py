class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: [ListNode]) -> [ListNode]:
    cur = head
    while cur:
        while cur.next and cur.next.val == cur.val:
            cur.next = cur.next.next
        cur = cur.next
    return head


head = [1, 1, 2]


# Output: [1,2]



