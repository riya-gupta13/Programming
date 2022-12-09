# https://takeuforward.org/data-structure/allocate-minimum-number-of-pages/
def books(A, B):
    def isAllocatepossible(A, pages, students):
        sumAllocated = 0
        allocatedStudent = 1
        for i in range(0, len(A)):
            if sumAllocated + A[i] > pages:
                allocatedStudent += 1
                sumAllocated = A[i]
                if sumAllocated > pages:
                    return False
            else:
                sumAllocated += A[i]
        if allocatedStudent > students:
            return False
        else:
            return True

    low = min(A)
    high = sum(A)
    res = -1

    while low <= high:
        mid = (low + high) // 2
        if isAllocatepossible(A, mid, B):
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res


A = [5, 17, 100, 11]
B = 4
print(books(A, B))
