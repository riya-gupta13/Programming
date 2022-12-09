
# inbuilt class for queue
from collections import deque

q = deque(maxlen=3)

q.append(1)
q.append(2)
q.append(3)
# q.clear() # will empty the queue
print(q.popleft())


