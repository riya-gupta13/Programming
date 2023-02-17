class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next

    # T-O(N), S-O(1)
    # Iteratively
    def reverseList(head):
        prev = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

    # Recursively
    def reverseListRec(self, head):
        if not head:
            return None
        newHead = head
        if head.next:
            newHead = self.reverseListRec(head.next)
            head.next.next = head
        head.next = None
        return (newHead)


l = ListNode(3)

L = LinkedList()
L.head = l
x = ListNode(4)
y = ListNode(5)
z = ListNode(6)
l.next = x
x.next = y
y.next = z
print(L.reverseListRec(l).val)









