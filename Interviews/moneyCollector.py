# Suppose we have a 2D matrix where each cell stores some coins.
# If we start from [0,0], and can only move right or down,
# we have to find the maximum number of coins we can collect by the bottom right corner.
def solve(A):
    for r in range(1, len(A)):
        A[r][0] += A[r - 1][0]
    for c in range(1, len(A[0])):
        A[0][c] += A[0][c - 1]
    for r in range(1, len(A)):
        for c in range(1, len(A[0])):
            A[r][c] += max(A[r - 1][c], A[r][c - 1])
    return A[-1][-1]


matrix = [[1, 4, 2, 2], [6, 0, 0, 5]]
print(solve(matrix))
