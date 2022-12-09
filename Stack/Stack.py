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

    def delete(self):
        self.list = None


customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
customStack.pop()
print(customStack.peek())
print(customStack)
