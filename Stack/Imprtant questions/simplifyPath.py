def simplifyPath(path: str) -> str:
    cur = ""
    stack = []
    for c in path + "/":
        if c == "/":
            if cur == "..":
                if stack:
                    stack.pop()
            elif cur != "" and cur != ".":
                stack.append(cur)
            cur = ""
        else:
            cur += c
    return "/" + "/".join(stack)


path = "/../abc/./def/"
print(simplifyPath(path))