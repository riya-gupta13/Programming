class ListNode:
    def __init__(self, data):
        self.next = None
        self.val = data


class LinkedList:
    def __init__(self, head=ListNode):
        self.head = head

    def print(self):
        temp = self.head
        while temp != None:
            print(temp.val, end=" ")
            temp = temp.next


# data = 2
l = ListNode(3)
x = ListNode(4)
y = ListNode(5)
z = ListNode(6)
l.next = x
x.next = y
y.next = z
li = LinkedList(l)
li.print()
