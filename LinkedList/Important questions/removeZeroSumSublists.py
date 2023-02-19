class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Firstly make a dummy Node of value 0 to connect in front of the LinkedList. Using pre we will store node with sum
# value upto that node. After storing we will again go through full linked list and if we get sum which already has
# stored in dic then we will move next pointer to that dic node's next node.
class Solution:
    def removeZeroSumSublists(self, head: ListNode):
        dummy = ListNode(0, head)
        pre = 0
        dic = {0: dummy}

        while head:
            pre += head.val
            dic[pre] = head
            head = head.next

        head = dummy
        pre = 0
        while head:
            pre += head.val
            head.next = dic[pre].next
            head = head.next

        return dummy.next
