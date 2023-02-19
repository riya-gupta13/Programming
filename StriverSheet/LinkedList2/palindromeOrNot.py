class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        head = prev

        return head

    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        slow.next = Solution.reverseList(slow.next)
        dummy = head
        while slow is not None:
            if dummy.val != slow.val:
                return False
            else:
                dummy = dummy.next
                slow = slow.next

        return True
