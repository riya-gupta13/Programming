def reverse(strng):
    n = len(strng)
    str = ''
    if n == 0:
        return ''
    if n == 1:
        return strng[n - 1]
    else:
        # print(strng[n - 1])
        str += strng[n - 1] + reverse(strng[:n - 1])
    return str


print(reverse("appmillers"))
