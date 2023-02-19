
def maxDepth(s: str) -> int:
    stack = []
    maxLen = 0
    for x in s:
        if x == '(':
            stack.append(x)
        elif x == ')':
            if len(stack) > maxLen:
                maxLen = len(stack)
            stack.pop()
    print(maxLen)
    return maxLen


s = "(1)+((2))+(((3)))"
# Output: 3
maxDepth(s)
