def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    swap = current = ListNode(0)
    arr = []
    while head:
        arr.append(head.val)
        head = head.next
    temp_val = arr[-k]
    arr[-k] = arr[k - 1]
    arr[k - 1] = temp_val

    for i in range(0, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next

    return swap.next