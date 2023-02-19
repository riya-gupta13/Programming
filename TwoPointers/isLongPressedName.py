def isLongPressedName(name: str, typed: str) -> bool:
    if len(name) > len(typed):
        return False
    a = 0
    s = ""
    for i in range(len(typed)):
        if i == 0 and typed[i] != name[a]:
            return False
        if typed[i] == name[a]:
            s += name[a]
            a += 1
            if a == len(name):
                a = len(name) - 1
        elif typed[i] == typed[i - 1]:
            continue
        else:
            return False
    if len(s) < len(name):
        return False
    return True


name = "alex"
typed = "aaleexeex"
print(isLongPressedName(name, typed))
