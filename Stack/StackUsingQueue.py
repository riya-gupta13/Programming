from collections import deque


class MyStack:

    def __init__(self):
        self.s = deque()

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        # approach except the last element we are pushing all elements again in s then we are popping last
        # q=[1,2,3]---- q=[3,1,2]--then pop --3 that's wht we wanted in stack to pop
        for i in range(len(self.s) - 1):
            self.push(self.s.popleft())
        return self.s.popleft()

    def top(self) -> int:
        return self.s[-1]

    def empty(self) -> bool:
        return len(self.s) == 0
