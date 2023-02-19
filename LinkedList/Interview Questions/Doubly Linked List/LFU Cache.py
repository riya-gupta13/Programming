#     * @param key: node key
#     * @param val: node value
#     * @param frequency: frequency count of current node
#     * (all nodes connected in same double linked list has same frequency)
#     * @param prev: previous pointer of current node
#     * @param next: next pointer of current node

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        self.frequency = 1


#     * @param listSize: current size of double linked list
#     * @param head: head node of double linked list
#     * @param tail: tail node of double linked list

class DLinkedList():
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.listSize = 0

    #  add new node into head of list and increase list size by 1
    def append(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.listSize += 1

    #  remove input node and decrease list size by 1
    def pop(self, node):
        prevNode = node.prev
        nextNode = node.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        self.listSize -= 1


#     * @param capacity: total capacity of LFU Cache
#     * @param curSize: current size of LFU cache
#     * @param minFrequency: frequency of the last linked list (the minimum frequency of entire LFU cache)
#     * @param cache: a hash map that has key to Node mapping, which used for storing all nodes by their keys
#     * @param frequencyMap: a hash map that has key to linked list mapping, which used for storing all
#     * double linked list by their frequencies


class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.curSize = 0
        self.minFreq = 0
        self.freqMap = {}  # freq, dLL
        self.cache = {}  # key,node

    # get node value by key, and then update node frequency as well as relocate that node **/
    def get(self, key: int) -> int:
        curNode = self.cache.get(key)
        if curNode is None:
            return -1
        else:
            self.updateNode(curNode)
            return curNode.val

    def updateNode(self, curNode):
        curFreq = curNode.frequency
        curList = self.freqMap.get(curFreq)
        # if current list is the last list which has the lowest frequency and current node is the only node in that
        # list we need to remove the entire list and then increase min frequency value by 1
        curList.pop(curNode)

        if curFreq == self.minFreq and curList.listSize == 0:
            self.minFreq += 1
        #  add current node to another list has current frequency + 1,
        #   if we do not have the list with this frequency, initialize it
        curNode.frequency += 1
        newList = self.freqMap.setdefault(curNode.frequency, DLinkedList())
        newList.append(curNode)
        self.freqMap.__setitem__(curNode.frequency, newList)

    #
    #       add new node into LFU cache, as well as double linked list
    #       condition 1: if LFU cache has input key, update node value and node position in list
    #       condition 2: if LFU cache does NOT have input key
    #        - sub condition 1: if LFU cache does NOT have enough space, remove the Least Recent Used node
    #       in minimum frequency list, then add new node
    #       - sub condition 2: if LFU cache has enough space, add new node directly
    #
    def put(self, key: int, value: int) -> None:
        #  corner case: check cache capacity initialization
        if self.cap == 0:
            return None
        if key in self.cache:
            curNode = self.cache.get(key)
            curNode.val = value
            self.updateNode(curNode)
        else:
            #  get minimum frequency list
            self.curSize += 1
            if self.curSize > self.cap:
                minFreqList = self.freqMap.get(self.minFreq)
                self.cache.pop(minFreqList.tail.prev.key)
                minFreqList.pop(minFreqList.tail.prev)
                self.curSize -= 1

            # reset min frequency to 1 because of adding new node
            self.minFreq = 1
            newNode = Node(key, value)

            #  get the list with frequency 1, and then add new node into the list, as well as into LFU cache
            curList = self.freqMap.setdefault(1, DLinkedList())
            curList.append(newNode)
            self.freqMap.__setitem__(1, curList)
            self.cache.__setitem__(key, newNode)
