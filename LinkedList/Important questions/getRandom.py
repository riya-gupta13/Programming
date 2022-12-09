import random


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def __init__(self, head: ListNode):
        self.head = head

    def getRandomBest(self) -> int:
        cur = self.head
        ans = 0
        # is for how much times that num is seen
        i = 0
        while cur:
            # capacity of the reservoir is 1, because we just need to return a single num
            if random.randint(0, i) == 0:
                # replace ans with i-th node.val with probability 1/i
                ans = cur.val
            cur = cur.next
            i += 1
        return ans

    def getRandom(self) -> int:
        # one approach
        # 1. find length by traversal
        # 2. then find random number and modulo length will give u index
        # 3.then traverse till taht index and return the node val
        # but in this approach evertything depends on length consider you dont know the length thats where
        # secnd approach comes-- Reservoir Sampling
        cur = self.head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        temp = random.random()
        n = temp % length
        cur = self.head
        for i in range(int(n)):
            cur = cur.next
        return cur.val
