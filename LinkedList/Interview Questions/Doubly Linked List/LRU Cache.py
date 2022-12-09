class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        # map key to node
        self.cache = {}
        self.left, = Node(0, 0)
        self.right = Node(0, 0)
        # left =LRU, rght=Most recent
        self.left.next = self.right
        self.right.prev = self.left

    # remove node from list
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = prev
        nxt.prev = prev

    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        # from the list and delete LRu from hashmap
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
