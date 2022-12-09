def longestValidParentheses(self, s: str) -> int:
    # approach
    # instead of storing () in stack will store the indices and when () cmes we pop
    # and we find the max index by sutracting the value till that index store the index till that in stack
    stack = []
    mx = 0
    for i, p in enumerate(s):
        if p == '(':
            stack.append(p)
        else:
            stack.pop()
            if not stack:
                stack.append(p)
            else:
                mx = max(mx, i - stack[-1])
    return mx


s = ")()())"
