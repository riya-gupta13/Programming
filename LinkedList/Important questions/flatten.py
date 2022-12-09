class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head):
        # approach
        # 1-2-3-4-5-6
        #     |
        #     7-8-9-12-13-None
        #       |
        #       10-11-None
        # stack-- wht we will do is frst put head in staack--[1]
        # then pop and put its nxt in stack---[2] noe chk its child no then put otherwise pop and put nxt
        # stack-[3],now pop and put is nxt also the child as child it has
        # sytack-[4,7]--now 7 will pop and its nxt will be put[4,8]..like this
        dummy = Node(0)
        cur = dummy
        stack = [head]
        while stack:
            temp = stack.pop()
            if temp.next:
                stack.append(temp.next)
            if temp.child:
                stack.append(temp.child)
            cur.next = temp
            temp.prev = cur
            temp.child = None
            cur = temp
        dummy.next.prev = None
        return dummy.next
