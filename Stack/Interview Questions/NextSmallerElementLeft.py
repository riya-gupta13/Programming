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


def nextSmallerElement(arr, n):
    stack = Stack()
    ans = [0] * len(arr)
    for i in arr:
        while not stack.isEmpty() and stack.peek() > i:
            stack.pop()
        if stack.isEmpty():
            ans[i] = -1
        else:
            ans[i] = stack.peek()
        stack.push(i)
