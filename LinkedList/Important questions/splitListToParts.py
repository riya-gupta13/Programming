class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: ListNode, k: int):
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next

        # calculate the base size and the number of parts contain extra number
        size, extraNodes = length // k, length % k

        # create empty list to store split parts
        res = [[] for _ in range(k)]

        # use two ptrs to split parts
        prev, cur = None, head

        for i in range(k):
            res[i] = cur
            # if this part contains extra number, it has (size+1) number
            for j in range(size + (1 if extraNodes > 0 else 0)):
                prev, cur = cur, cur.next
            if prev:
                prev.next = None
            extraNodes -= 1

        return res