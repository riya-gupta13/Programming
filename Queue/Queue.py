class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        data = [str(i) for i in self.items]
        return " ".join(data)

    def isEmpty(self):
        if not self.items:
            return True
        else:
            return False

    def enqueue(self, value):
        self.items.append(value)
        return "Item is successfully added"

    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.items[0]

    def delete(self):
        self.items = []


q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.dequeue()
print(q)
print(q.peek())
