def removeOuterParentheses(s: str) -> str:
    l = list(s)
    count = 0
    li = []
    for i in l:
        if i == ')':
            count -= 1.
        if count > 0:
            li.append(i)
        if i == '(':
            count += 1
    print("".join(li))
    return "".join(li)


s = "(()())(())"
# Output: "()()()"
removeOuterParentheses(s)
