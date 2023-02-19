class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            curNode = curNode.next


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(i) for i in self.LinkedList]
        return "\n".join(values)

    def isEmpty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False

    def push(self, value):
        newNode = Node(value)
        newNode.next = self.LinkedList.head
        self.LinkedList.head = newNode

    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        nodeVal = self.LinkedList.head
        self.LinkedList.head = self.LinkedList.head.next
        return nodeVal

    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack"
        else:
            return self.LinkedList.head.value

    def delete(self):
        self.LinkedList.head = None


customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)

print(customStack.peek())
