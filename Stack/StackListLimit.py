class Stack:
    def __init__(self,maxsize):
        self.maxsize=maxsize
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

    def isFull(self):
        if len(self.list)==self.maxsize:
            return "Stack is Full"
        else:
            return "Stack is not Full"

    def push(self, value):
        if self.isFull():
            return "Stack is Full"
        else:
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