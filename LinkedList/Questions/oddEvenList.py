class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: [ListNode]) -> [ListNode]:
        cur = head
        odd = []
        even = []
        l = []
        while cur:
            l.append(cur.val)
            cur = cur.next
        print(l)
        if len(l) == 0:
            return cur
        for i in range(0, len(l)):
            if i % 2 == 0:
                odd.append(l[i])
            else:
                even.append(l[i])
        print(odd, even)
        final = odd + even
        print(final)
        cur = ListNode(final[0])
        head = cur
        for i in final[1:]:
            temp = ListNode(i)
            cur.next = temp
            cur = temp
        return head
