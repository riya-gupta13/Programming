# Priority queue is a queue in which elemnts are popped based on priority
# if elements have same priority then order is considered frst
# Priority is decided by you it can be low elemnt--high priority or high elemnt-high priority
# or u can use tuple to add the priority and the elemnt

# Implemenation Using List
# when we add elemnt to list sort it
q = []
q.append(1)
q.append(2)
q.sort()
q.append(0)
q.sort()
q.pop(0)
# this is worst mthd to implement priority queue

# using PriorityQueue from Queue module
from queue import PriorityQueue

# in this low element high priority
q = PriorityQueue()
q.put(1)
q.put(10)
q.put(6)
q.get()

# using tuple
q = []
q.append((1, "Riya"))
q.append((3, 'Me'))
q.sort()
q.pop(0)
