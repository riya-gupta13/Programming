import heapq
from collections import Counter, deque


def leastInterval(self, tasks: list[str], n: int) -> int:
    # approach we will be using macHeap and queue maxHeap for the tasks count and queue for idletime so what we are
    # doing is we are not considering chars just take its count and push in heap as in python we don't have minHeap,
    # so we use maxHeap and that's why while making heap we'll add with negative sign so that when we heapify max
    # should be frst then in queue well be storing pair[cnt,idleTime], where cnt will be decreasing everytime as that
    # task will be performed and idletime is the time +n that is when is the nextTime it can be performed
    # if cnt becomes 0 thn we will not add as tasks are finished for tht

    count = Counter(tasks)
    maxHeap = [-cnt for cnt in count.values()]
    heapq.heapify(maxHeap)

    time = 0
    q = deque()
    while maxHeap or q:
        time += 1
        if maxHeap:
            cnt = 1 + heapq.heappop(maxHeap)
            # if task count is not 0 then append
            if cnt:
                q.append([cnt, time + n])
        # if q is not empty and the idletime is equal to time means we can perform that task again
        # so push in heap
        if q and q[0][1] == time:
            heapq.heappush(maxHeap, q.popleft()[0])
    return time
