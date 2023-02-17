def getIntersectionNode(self, headA, headB):
    # approach
    # frst-- we can use hashset and do
    # scnd=-- bring tghe lrger list pointer at same distnce from common--as find lengths of both then diff of them is the nodes
    # difference move in lrger tht distnce then cmpare in both

    # optimal approach
    # move in both list one one pointer if secnd lists pointer bcmes null point to first list head and same for frst piint to secnd head
    # then u will noticw thy will cme at same level and ehn frst nd scnd equal return
    l1 = headA
    l2 = headB
    while l1 != l2:
        if l1:
            l1 = l1.next
        else:
            l1 = headB
        if l2:
            l2 = l2.next
        else:
            l2 = headA
    return l1



