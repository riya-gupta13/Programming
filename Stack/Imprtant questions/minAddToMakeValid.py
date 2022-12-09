def minAddToMakeValid(s: str) -> int:
    stack = []
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if stack:
                top = stack[-1]
                print(stack)
                if i == ')' and top == '(':
                    stack.pop(-1)
                else:
                    stack.append(i)
            else:
                stack.append(i)
    return len(stack)


s = ")())("
print(minAddToMakeValid(s))
