import queue as q

Queue = q.Queue(maxsize=3)

print(Queue.put(1))
print(Queue.put(2))
print(Queue.put(3))
print(Queue.qsize())
print(Queue.get())  # gives frst elemnt and pops tht elem
print(Queue.full())
print(Queue.empty())
