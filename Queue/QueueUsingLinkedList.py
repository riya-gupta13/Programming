class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next


class Queue:
    def __init__(self):
        self.Linkedlist = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.Linkedlist]
        return ' '.join(values)

    def isEmpty(self):
        if self.Linkedlist.head is None:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.Linkedlist.head is None:
            self.Linkedlist.head = Node(value)
        else:
            newNode = Node(value)
            cur = self.Linkedlist.head
            while cur.next:
                cur = cur.next
            cur.next = newNode
            cur.next.next = None

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            temp = self.Linkedlist.head
            if self.Linkedlist.head.next is None:
                self.Linkedlist.head = None
            else:
                self.Linkedlist.head = self.Linkedlist.head.next
            return temp

    def peek(self):
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            return self.Linkedlist.head

    def delete(self):
        self.Linkedlist.head = None


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q)
print(q.dequeue())
print(q.peek())
