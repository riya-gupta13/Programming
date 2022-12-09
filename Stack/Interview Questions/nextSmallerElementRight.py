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


def nextSmallerElementRight(arr, n):
    stack = Stack()
    ans = [0] * len(arr)
    for i in range(len(arr) - 1, -1, -1):
        while not stack.isEmpty() and stack.peek() > arr[i]:
            stack.pop()
        if stack.isEmpty():
            ans[i] = -1
        else:
            ans[i] = stack.peek()
        stack.push(arr[i])
    return ans


arr = [2, 4, 6, 1, 3, 9, 7]
print(nextSmallerElementRight(arr, 7))
