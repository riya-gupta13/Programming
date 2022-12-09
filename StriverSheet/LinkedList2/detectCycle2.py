class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(head: ListNode):
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        pointer = head
        while pointer != fast:
            pointer = pointer.next
            fast = fast.next
        return pointer


if __name__ == '__main__':
    head = [3, 2, 0, -4]
    pos = 1
    receiveNode = Solution.detectCycle(head)
