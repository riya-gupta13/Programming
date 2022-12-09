class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: [ListNode]) -> int:
        cur = head
        l = []
        while cur:
            l.append(cur.val)
            cur = cur.next
        print(l)
        n = len(l)
        frst = l[:(n // 2)]
        secnd = l[(n // 2):]
        print(frst, secnd)
        secnd = secnd[::-1]
        max = 0
        for i in range(0, len(frst)):
            sum = frst[i] + secnd[i]
            if max <= sum:
                max = sum
        return (max)
