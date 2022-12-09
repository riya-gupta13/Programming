class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def nodesBetweenCriticalPoints(self, head: ListNode):
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        cur = head.next
        prev = head
        maxMin = []
        count = 1
        while cur.next:
            if cur.val < cur.next.val and cur.val < prev.val:
                maxMin.append(count)
            elif cur.val > cur.next.val and cur.val > prev.val:
                maxMin.append(count)
            prev = cur
            cur = cur.next
            count += 1
        if len(maxMin) < 2:
            return [-1, -1]
        res = [float('inf'), float('-inf')]
        for i in range(1, len(maxMin)):
            res[0] = min(res[0], maxMin[i] - maxMin[i - 1])
        res[1] = maxMin[-1] - maxMin[0]
        return res

