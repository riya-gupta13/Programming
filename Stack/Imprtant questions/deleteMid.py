import math


class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        self.list.reverse()
        values = []
        for i in self.list:
            values.append(str(i))
        return "\n".join(values)

    def isEmpty(self):
        if not self.list:
            return True
        else:
            return False

    def push(self, value):
        self.list.append(value)
        return "The element was successfully inserted"

    def pop(self):
        if self.isEmpty():
            return "Stack is already empty"
        else:
            return self.list.pop()

    def peek(self):
        if self.isEmpty():
            return "Stack is already empty"
        else:
            return self.list[len(self.list) - 1]


def deleteMiddle(s, i, n):
    if i == n:
        return
    x = s.peek()
    s.pop()
    deleteMiddle(s, i + 1, n)
    if i == n // 2:
        s.push(x)
    print(s)


def deleteMid(s, sizeOfStack):
    deleteMiddle(s, 0, sizeOfStack)


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.push(5)
print(deleteMid(s, 5))
