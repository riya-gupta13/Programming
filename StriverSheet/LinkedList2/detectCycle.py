class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def detectCycle(self, head: [ListNode]) -> [ListNode]:
    track = set()
    while head:
        if head not in track:
            track.add(head)
        else:
            return head
        head = head.next