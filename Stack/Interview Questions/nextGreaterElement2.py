class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        self.list.reverse()
        values = []
        for i in self.list:
            values.append(str(i))
        return " ".join(values)

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


def nextGreaterElements(nums):
    ans = [0] * len(nums)
    s = Stack()
    n = len(nums)
    for i in range(2 * n - 1, -1, -1):
        while (not s.isEmpty()) and s.peek() <= nums[i % n]:
            s.pop()
        # print(s)
        if i < n:
            if not s.isEmpty():
                ans[i] = s.peek()
            else:
                ans[i] = -1
        s.push(nums[i % n])
    print(ans)


# [2,3,4,-1,4]
nums = [5, 4, 3, 2, 1]
nextGreaterElements(nums)
