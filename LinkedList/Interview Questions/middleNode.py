class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def middleNodeBestApproach(head: ListNode):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def middleNode(self, head: ListNode) -> ListNode:
    cur = head
    count = 0
    while cur:
        count += 1
        cur = cur.next
    mid = count // 2
    ans = head
    l = 0
    while l != mid:
        ans = ans.next
        l += 1
    return ans
