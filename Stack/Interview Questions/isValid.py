def isValid(s: str) -> bool:
    ans = []
    for i in s:
        if i == '(' or i == '[' or i == '{':
            ans.append(i)
        else:
            top = ans[len(ans) - 1]
            if top == '(' and i == ')':
                ans.pop(0)
            elif top == '[' and i == ']':
                ans.pop(0)
            elif top == '{' and i == '}':
                ans.pop(0)
            else:
                return False
    if not ans:
        return True

# "()"
# "({[})][]{}"
# "(]"
# "["
# "[]{"
# "{{{]"
# "}}"
# "}{"
s = "()"
# Output: true
print(isValid(s))