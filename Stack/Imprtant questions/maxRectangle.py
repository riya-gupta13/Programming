def maxArea(M, n, m):
    #     approach
    # same as largest rectangle area question
    # wht we are doing is we are passing one one row data to that fxn
    # but for that we need to see its height and width thats based on 1 if 1 add else 0
    height = [0] * m
    maxAr = 0
    for i in range(n):
        for j in range(m):
            if M[i][j] == 1:
                height[j] += 1
            else:
                height[j] = 0
        area = largestRectangleArea(height)
        # print(area)
        maxAr = max(maxAr, area)
    return maxAr


# https://leetcode.com/problems/largest-rectangle-in-histogram/
def largestRectangleArea(heights) -> int:
    stack = []  # pair(index,heights)
    maxArea = 0
    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            index, height = stack.pop()
            maxArea = max(maxArea, height * (i - index))
            start = index
        stack.append((start, h))
    for i, h in stack:
        maxArea = max(maxArea, h * (len(heights) - i))
    return maxArea


n = 4
m = 4
M = [[0, 1, 1, 0],
     [1, 1, 1, 1],
     [1, 1, 1, 1],
     [1, 1, 0, 0]]
print(maxArea(M,n,m))