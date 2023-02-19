class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            v = min(val, self.minStack[-1])
        else:
            v = val
        self.minStack.append(v)

    def pop(self) -> None:
        self.stack.pop(-1)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        # not optimal approach --O(n) return min(self.stack) we should is created 1 more stack in which we will take
        # min of value which we are pushing and the top of min stack sio that we have min value for every corresponding
        # value, and then we can return the top of min-stack
        return self.minStack[-1]
