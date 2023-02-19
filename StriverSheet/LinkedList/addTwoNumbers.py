class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        temp = dummy
        carry = 0
        while l1.next is not None or l2.next is not None or carry != 0:
            sum = 0
            if l1.next is not None:
                sum += l1.val
                l1 = l1.next
            if l2.next is not None:
                sum += l2.val
                l2 = l2.next
            sum += carry
            carry = sum // 10
            node = ListNode(sum % 10)
            temp.next = node
            temp = temp.next
        return dummy.next


l1 = [2, 4, 3]
l2 = [5, 6, 4]

# Output: [7,0,8]
