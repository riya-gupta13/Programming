def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    number1 = ""
    number2 = ""
    while l1:
        number1 = number1 + str(l1.val)
        l1 = l1.next
    while l2:
        number2 = number2 + str(l2.val)
        l2 = l2.next
    total = list(str(int(number1[::-1]) + int(number2[::-1])))
    total.reverse()
    final = [int(x) for x in total]

    curr = ListNode(final[0])
    head = curr
    for i in final[1:]:
        temp = ListNode(i)
        curr.next = temp
        curr = temp
    return head