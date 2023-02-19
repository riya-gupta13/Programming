class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


def copyRandomList(self, head: Node) -> Node:
    # approach
    # frst we will make a deep copy of every node and store in hashmap
    # then we will iterate through the list and get the cop node then we can points its next and random pointer
    # that too we can get from hashmap
    # here we are storing that None:None as if cur.next is None then it shld be set to None
    oldToCopy = {None: None}
    cur = head
    while cur:
        oldToCopy[cur] = Node(cur.val)
        cur = cur.next
    cur = head
    while cur:
        copy = oldToCopy[cur]
        copy.next = oldToCopy[cur.next]
        copy.random = oldToCopy[cur.random]
        cur = cur.next
    return oldToCopy[head]
