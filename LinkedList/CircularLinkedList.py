class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            newNode.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = newNode
            newNode.next = self.head

    def prepend(self, val):
        newNode = Node(val)
        cur = self.head
        newNode.next = self.head

        if not self.head:
            self.head = newNode
            newNode.next = self.head
        else:
            while cur.next != self.head:
                cur = cur.next
            cur.next = newNode
        self.head = newNode

    def printList(self):
        cur = self.head
        while cur:
            print(cur.value)
            cur = cur.next
            if cur == self.head:
                break

    def removeByKey(self, key):
        if self.head.value == key:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.value == key:
                    prev.next = cur.next
                    cur = cur.next

    def removeNode(self, node):
        if self.head == node:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = self.head.next
            self.head = self.head.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur == node:
                    prev.next = cur.next
                    cur = cur.next

    def __len__(self):
        count = 0
        cur = self.head
        while cur:
            cur = cur.next
            count += 1
            if cur == self.head:
                break
        return count

    def splitList(self):
        size = len(cl)
        if size == 0:
            return None
        if size == 1:
            return self.head
        mid = size // 2
        cur = self.head
        prev = None
        count = 0
        while cur and count < mid:
            count += 1
            prev = cur
            cur = cur.next
        prev.next = self.head

        splitCList = CircularLinkedList()
        while cur.next != self.head:
            splitCList.append(cur.value)
            cur = cur.next
        splitCList.append(cur.value)

        self.printList()
        print("\n")
        splitCList.printList()

    def is_Circular(self, inputList):
        cur = inputList.head
        while cur.next:
            cur = cur.next
            if cur.next == inputList.head:
                return True
        return False

    # is a problem where step is given and once we reach that step we need to remove that elemnt, follow this until
    # it only has one elemnt
    def josephus_problem(self, step):
        cur = self.head
        while len(self) > 1:
            count = 1
            while count != step:
                cur = cur.next
                count += 1
            print("Removed " + str(cur.value))
            self.removeNode(cur)
            cur = cur.next


cl = CircularLinkedList()
cl.append(1)
cl.append(2)
cl.append(3)
cl.append(4)

# cl.printList()
# cl.remove(3)
# print(len(cl))
# cl.splitList()
cl.josephus_problem(2)
cl.printList()

