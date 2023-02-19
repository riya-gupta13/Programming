# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    l = LinkedList()
    head = [4, 5, 1, 9]
    # l.print()
    node = Node(5,None)
    l.deleteNode(node)

# Output: [4, 1, 9]
