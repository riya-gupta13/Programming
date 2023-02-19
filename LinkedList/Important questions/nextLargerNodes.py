class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def nextLargerNodes(self, head: ListNode):
    if not head:
        return head

    def length(cur, l):
        while cur:
            l += 1
            cur = cur.next
        return l

    def reverse(cur, prev):
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        return prev

    curr = head
    l = 0
    len = length(curr, l)
    cur = head
    prev = None
    list = reverse(cur, prev)
    ans = [None] * len
    i = 0
    stack = []
    while list:
        while stack and stack[-1] <= list.val:
            stack.pop()
        if stack:
            ans[i] = stack[-1]
        else:
            ans[i] = 0
        stack.append(list.val)
        i += 1
        list = list.next
    return ans[::-1]