class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: [ListNode]) -> [ListNode]:
        cur = head
        l = []
        while cur:
            l.append(cur.val)
            cur = cur.next
        if len(l) % 2 == 0:
            mid = int(len(l) // 2)
            l.pop(mid)
        else:
            mid = int(len(l) // 2)
            l.pop(mid)
        cur = ListNode(l[0])
        head = cur
        for i in l[1:]:
            temp = ListNode(i)
            cur.next = temp
            cur = temp
        return head
