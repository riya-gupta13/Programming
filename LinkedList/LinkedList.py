class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def get(self, index):
        if index < 0 or index > self.getLength():
            raise Exception("Invalid Index")
        temp = self.head
        for i in range(index):
            temp = temp.next
        print(temp.data)
        return temp

    def set(self,index,value):
        temp=self.get(index)
        if temp!=None:
            temp.data=value

        print(temp.data)

    def insert_at_begin(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return ""
        else:
            itr = self.head
            while itr:
                print(str(itr.data))
                itr = itr.next

    def insert_at_end(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
            node.next = None
        else:
            itr = self.head
            while itr.next:
                itr = itr.next
            itr.next = node
            itr.next.next = None

    def getLength(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_values(self, data_list):
        self.head = None
        for d in data_list:
            self.insert_at_end(d)

    def removeByIndex(self, index):
        if index < 0 or index > self.getLength():
            raise Exception("Invalid Index")
        else:
            count = 0
            itr = self.head
            while itr:
                if count == index - 1:
                    itr.next = itr.next.next
                    break
                itr = itr.next
                count += 1

    def insert_at_index(self, index, data):
        if index < 0 or index > self.getLength():
            raise Exception("Invalid Index")
        if index == 0:
            self.insert_at_begin(data)
        else:
            count = 0
            itr = self.head
            while itr:
                if count == index - 1:
                    node = Node(data)
                    node.next = itr.next
                    itr.next = node
                itr = itr.next
                count += 1

    def insert_after_value(self, data_after, data_to_insert):
        itr = self.head
        print(itr.data)
        while itr:
            if itr.data == data_after:
                node = Node(data_to_insert)
                node.next = itr.next
                itr.next = node
            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        else:
            itr = self.head
            while itr:
                if itr.next.data == data:
                    itr.next = itr.next.next
                    break
                itr = itr.next

    def nodes_swap(self, key1, key2):
        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key1:
            prev_1 = curr_1
            curr_1 = curr_1.next
        curr_2 = self.head
        prev_2 = None
        while curr_2 and curr_2.data != key2:
            prev_2 = curr_2
            curr_2 = curr_2.next
        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2
        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1
        curr_1.next, curr_2.next = curr_2.next, curr_1.next

    def reverse_iterative(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def merge_two_lists(self, llist2):
        global new_head
        p = self.head
        q = llist2.head
        s = None
        if not p:
            return q
        if not q:
            return p
        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s
        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        return new_head

    def remove_dup(self):
        cur = self.head
        prev = None
        dup = dict()
        while cur:
            if cur.data in dup:
                prev.next = cur.next
                cur = None
            else:
                dup[cur] = 1
                prev = cur
            cur = prev.next

    def print_nth_from_last_node(self, n):
        cur = self.head
        total_len = self.getLength()
        while cur:
            if total_len == n:
                print(cur.data)
            total_len -= 1
            cur = cur.next
        if cur is None:
            return

    def count_occurrences(self, data):
        cur = self.head
        count = 0
        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next
        return count

    def rotate(self, k):
        p = self.head
        q = self.head
        count = 0
        prev = None
        while p and count < k:
            prev = p
            p = p.next
            q = q.next
            count += 1
        p = prev
        while q:
            prev = q
            q = q.next
        q = prev
        q.next = self.head
        self.head = p.next
        p.next = None

    def is_palindrome(self):
        p = self.head
        s = ""
        while p:
            s += p.data
            p = p.next
        return s == s[::-1]

    def move_last_to_head(self):
        second_last = None
        last = self.head
        while last.next:
            second_last = last
            last = last.next
        last.next = self.head
        second_last.next = None
        self.head = last

    def sum_two_lists(self, llist):
        p = self.head
        q = llist.head
        carry = 0
        sum_list = LinkedList()
        while p or q:
            if not p:
                i = 0
            else:
                i = p.data
            if not q:
                j = 0
            else:
                j = q.data
            s = i + j + carry
            if s >= 10:
                carry = 1
                remainder = s % 10
                sum_list.insert_at_end(remainder)
            else:
                carry = 0
                sum_list.insert_at_end(s)
            if p:
                p = p.next
            if q:
                q = q.next
        sum_list.print()


if __name__ == '__main__':
    l = LinkedList()
    l.insert_values([0,1,2])
    # l.get(2)
    # l.set(2,6)
    # l.insert_values(['r', 'a', 'd', 'a', 'r'])
    # l.insert_at_begin(23)
    # l.insert_at_begin(45)
    # l.insert_at_end(34)
    # l.insert_at_end(38)
    # l.insert_at_index(3,67)
    # l.insert_after_value(23, 87)
    # l.remove_by_value(3)
    # l.nodes_swap(54, 14)
    # l.reverse_iterative()
    # l2 = LinkedList()
    # l2.insert_values([5, 7, 8])
    # l.merge_two_lists(l2)
    # l.print_nth_from_last_node(2)
    # print(l.count_occurrences(54))
    l.print()
    l.rotate(4)
    # print(l.is_palindrome())
    # l.move_last_to_head()
    # l.sum_two_lists(l2)
    l.print()
