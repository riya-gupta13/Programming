def removeA(ans, s):
    if len(s) == 0:
        print(ans)
        return
    ch = s[0]
    if ch == 'a':
        removeA(ans, s[1:])
    else:
        removeA(ans + ch, s[1:])


def removeAReturn(s):
    if len(s) == 0:
        return ''
    ch = s[0]
    if ch == 'a':
        return removeAReturn(s[1:])
    else:
        return ch + removeAReturn(s[1:])


ans = ''
removeA(ans, 'baccda')
print(ans)

print(removeAReturn('baccda'))
