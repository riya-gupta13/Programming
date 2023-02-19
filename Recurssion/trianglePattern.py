def trianglePattern(r, c):
    if r == 0:
        return
    if c < r:
        print('*', end=' ')
        trianglePattern(r, c + 1)
    else:
        print(' ')
        trianglePattern(r - 1, 0)


def trianglePattern2(r, c):
    if r == 0:
        return
    if c < r:
        trianglePattern2(r, c + 1)
        print('*', end=' ')

    else:
        trianglePattern2(r - 1, 0)
        print(' ')

trianglePattern(4, 0)

trianglePattern2(4, 0)
