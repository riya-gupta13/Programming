class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        # self.length=1

    def getLength(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def get(self, index):
        if index < 0 or index >= self.getLength():
            raise Exception("Invalid Index")
        temp = self.head

        if index < self.getLength() / 2:
            for i in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for i in range(self.getLength() - 1, index, -1):
                temp = temp.prev
        return temp

    def set(self, index, data):
        ind = self.get(index)
        if ind is not None:
            ind.data = data

    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            node.prev = None
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = node
            node.prev = itr
            node.next = None

    def insert_at_begin(self, data):
        node = Node(data)
        if self.head is None:
            # node.next = self.head
            self.head = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
            node.prev = None

    def insert_after_value(self, key, data):
        node = Node(data)
        if self.head.data == key and self.head.next == None:
            self.insert_at_end(data)
        else:
            itr = self.head
            while itr:
                if itr.data == key:
                    next = itr.next
                    next.prev = node
                    itr.next = node
                    node.prev = itr
                    node.next = next
                itr = itr.next

    def insert_before_value(self, key, data):
        node = Node(data)
        if self.head.data == key and self.head.prev == None:
            self.insert_at_begin(data)
        else:
            itr = self.head
            while itr:
                if itr.data == key:
                    prev = itr.prev
                    prev.next = node
                    itr.prev = node
                    node.next = itr
                    node.prev = prev
                itr = itr.next

    def print(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            itr = self.head
            while itr:
                print(itr.data)
                itr = itr.next

    def delete_by_value(self, key):
        itr = self.head
        while itr:
            if itr.data == key and itr == self.head:
                if not itr.next:
                    itr = None
                    self.head = None
                    return
                else:
                    next = itr.next
                    itr.next = None
                    next.prev = None
                    itr = None
                    self.head = next
                    return
            elif itr.data == key:
                if itr.next:
                    next = itr.next
                    prev = itr.prev
                    prev.next = next
                    next.prev = prev
                    itr.next = None
                    itr.prev = None
                    itr = None
                    return
                else:
                    prev = itr.prev
                    prev.next = None
                    itr.prev = None
                    itr = None
                    return
            itr = itr.next

    def reverse(self):
        itr = self.head
        temp = None
        while itr:
            temp = itr.prev
            itr.prev = itr.next
            itr.next = temp
            itr = itr.prev
        if temp:
            self.head = temp.prev

    def delete_by_node(self, node):
        itr = self.head
        while itr:
            if itr == node and itr == self.head:
                if not itr.next:
                    itr = None
                    self.head = None
                    return
                else:
                    next = itr.next
                    itr.next = None
                    next.prev = None
                    itr = None
                    self.head = next
                    return
            elif itr == node:
                if itr.next:
                    next = itr.next
                    prev = itr.prev
                    prev.next = next
                    next.prev = prev
                    itr.next = None
                    itr.prev = None
                    itr = None
                    return
                else:
                    prev = itr.prev
                    prev.next = None
                    itr.prev = None
                    itr = None
                    return
            itr = itr.next

    def reverse(self):
        itr = self.head
        temp = None
        while itr:
            temp = itr.prev
            itr.prev = itr.next
            itr.next = temp
            itr = itr.prev
        if temp:
            self.head = temp.prev

    def remove_duplicates(self):
        itr = self.head
        seen = dict()
        while itr:
            if itr.data not in seen:
                seen[itr.data] = 1
                itr = itr.next
            else:
                nxt = itr.next
                self.delete_by_node(itr)
                itr = nxt

    def pairs_with_sum(self, sum):
        p = self.head
        q = None
        while p:
            q = p.next
            while q:
                if p.data + q.data == sum:
                    print("(" + str(p.data) + "," + str(q.data) + ")")
                q = q.next
            p = p.next


if __name__ == '__main__':
    d = DoubleLinkedList()
    d.insert_at_end(5)
    d.insert_at_end(2)
    d.insert_at_end(1)
    d.insert_at_end(4)
    d.insert_at_end(6)
    d.insert_at_end(8)
    d.insert_at_begin(4)
    print(d.get(3))
    d.set(3,9)
    # d.insert_before_value(8, 9)
    # d.delete_by_value(6)
    # d.reverse()
    # d.remove_duplicates()
    # d.pairs_with_sum(7)
    d.print()
