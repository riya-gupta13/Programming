class Queue:
    def __init__(self, maxsize):
        self.items = maxsize * [None]
        self.maxsize = maxsize
        self.top = -1
        self.start = -1

    def __str__(self):
        data = [str(i) for i in self.items]
        return " ".join(data)

    def isFull(self):
        if self.top + 1 == self.maxsize and self.start == 0:
            return True
        if self.top + 1 == self.start:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.isFull():
            return "Queue is full"
        else:
            if self.top + 1 == self.maxsize:  # last elemnt
                self.top = 0
            else:
                self.top += 1  # increase top
                # if we are adding first elmnt to empty quue to strt needs to incremntsd
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "The element is inserted at the end of Queue"

    def dequeue(self):
        if self.isEmpty():
            return "Queue is already empty"
        else:
            firstElement = self.items[self.start]
            start = self.start
            if self.start == self.top:
                self.start = -1  # means only one elemmnt in queue
                self.top = -1  # so queue is empty thst why -1,-1(last elmnt)
            else:
                # first elemnt points to last elemnt thn pointng it to come to begnng
                if self.start + 1 == self.maxsize:
                    self.start = 0
                else:
                    self.start += 1
                self.items[start] = None
                return firstElement

    def peek(self):
        if self.isEmpty():
            return "Queue is already empty"
        else:
            return self.items[self.start]

    def delete(self):
        self.items = self.maxsize * [None]
        self.top = -1
        self.start = -1
