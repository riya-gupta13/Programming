import collections


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
    cur = head
    l = []
    while cur:
        l.append(cur.val)
        cur = cur.next
    d = collections.Counter(l)
    new_list = []
    for i in d:
        if d[i] == 1:
            new_list.append(i)
    final = sorted(new_list)
    if len(final) == 0:
        return cur
    cur = ListNode(final[0])
    head = cur
    for i in final[1:]:
        temp = ListNode(i)
        cur.next = temp
        cur = temp
    return head
