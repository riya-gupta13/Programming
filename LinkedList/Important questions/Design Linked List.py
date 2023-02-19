class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = None

    def __str__(self):
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next

    def get(self, index: int) -> int:
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        if index < 0 or index >= count:
            return -1
        else:
            cur = self.head
            for i in range(index):
                cur = cur.next
            return cur.val

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)
        node.next = self.head
        self.head = node

    def addAtTail(self, val: int) -> None:
        node = ListNode(val)
        if self.head is None:
            self.head = node
            node.next = None
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
            cur.next.next = None

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        if index < 0 or index > count:
            return None
        elif index == 0:
            self.addAtHead(val)
        elif index == count:
            self.addAtTail(val)
        else:
            count = 0
            cur = self.head
            while cur:
                if count == index - 1:
                    node = ListNode(val)
                    node.next = cur.next
                    cur.next = node
                cur = cur.next
                count += 1

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        if index < 0 or index >= count:
            return None
        if index == 0:
            self.head = self.head.next
        else:
            cur = self.head
            c = 0
            while cur:
                if c == index - 1:
                    cur.next = cur.next.next
                    break
                cur = cur.next
                c += 1
            count -= 1  # decrement size of list

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
