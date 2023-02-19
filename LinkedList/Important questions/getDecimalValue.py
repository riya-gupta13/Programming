class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cur = head
        temp = ''
        while cur:
            temp += str(cur.val)
            cur = cur.next
        print(temp)
        ans= int(temp, 2)

