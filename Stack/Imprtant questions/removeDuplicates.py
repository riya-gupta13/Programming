def removeDuplicates(s: str) -> str:
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        elif stack is not None and stack[-1] != i:
            stack.append(i)
        else:
            stack.pop(-1)
    print(stack)
    return "".join(stack)


s = "azzzzzzzzx"
print(removeDuplicates(s))
