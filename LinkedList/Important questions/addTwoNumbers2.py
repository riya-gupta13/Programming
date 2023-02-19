class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
    stack1 = []
    stack2 = []
    while l1:
        stack1.append(l1.val)
        l1 = l1.next
    while l2:
        stack2.append(l2.val)
        l2 = l2.next
    carry = 0
    temp = None
    while stack1 or stack2 or carry:
        if stack1:
            i = stack1.pop()
        else:
            i = 0
        if stack2:
            j = stack2.pop()
        else:
            j = 0
        sum = i + j + carry
        node = ListNode(sum % 10)
        node.next = temp
        temp = node
        carry = sum // 10

    return temp
