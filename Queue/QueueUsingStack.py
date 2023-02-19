class MyQueue:

    def __init__(self):
        self.stack = []
        self.stack2 = []

    def push(self, x: int) -> None:
        return self.stack.append(x)

    def pop(self) -> int:
        while self.stack:
            self.stack2.append(self.stack.pop())
        ans = self.stack2.pop()
        while self.stack2:
            self.stack.append(self.stack2.pop())
        return ans

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        if len(self.stack) == 0 and len(self.stack2) == 0:
            return True
        else:
            return False


s = MyQueue()
s.push(1)
s.push(2)
s.pop()
