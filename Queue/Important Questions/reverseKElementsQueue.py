import collections


# GEEKSFORGEEKS
# https://practice.geeksforgeeks.org/problems/reverse-first-k-elements-of-queue/1
def modifyQueue(q, k):
    # code here
    stack = []
    que = q[:k]
    for i in range(0, k):
        stack.append(que.pop(0))
    queue = []
    for i in range(0, k):
        queue.append(stack.pop(-1))
    queue.extend(q[k:])
    return queue


q = [1, 2, 3, 4, 5]
k = 3
modifyQueue(q, k)
