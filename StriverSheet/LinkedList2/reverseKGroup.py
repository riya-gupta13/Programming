class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(head: ListNode, k: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        if not head or k == 1:
            return head
        cur = dummy
        # nxt = dummy
        prev = dummy
        count = 0
        while cur.next:
            count += 1
            cur = cur.next
        while count >= k:
            cur = prev.next
            nxt = cur.next
            for i in range(1, k):
                cur.next = nxt.next
                nxt.next = prev.next
                prev.next = nxt
                nxt = cur.next
            prev = cur
            count -= 1
        return dummy.next


head = [1, 2, 3, 4, 5]
k = 2
# Output: [2,1,4,3,5]
Solution.reverseKGroup(head, k)
