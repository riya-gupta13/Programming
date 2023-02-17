class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def sortList(self, head: [ListNode]) -> [ListNode]:
    if not head or not head.next:
        return head
    else:
        left = head
        right = self.getMid(head)
        tmp = right.next
        right.next = None
        right = tmp
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)


def getMid(self, head):
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge(self, l1, l2):
    temp = dummyNode = ListNode()
    while l1 and l2:
        if l1.val <= l2.val:
            temp.next = l1
            l1 = l1.next
        else:
            temp.next = l2
            l2 = l2.next
        temp = temp.next
    if l1:
        temp.next = l1
    if l2:
        temp.next = l2
    return dummyNode.next

