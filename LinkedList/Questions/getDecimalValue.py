def getDecimalValue(self, head: ListNode) -> int:
    temp = head
    s = ''
    while temp:
        s += str(temp.val)
        temp = temp.next
    ans = int(s, 2)
    return (ans)

