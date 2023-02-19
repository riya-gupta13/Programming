def pattern():
    n = 5
    for row in range(1, n + 1):
        for col in range(n, 0, -1):
            print('*', end=' ')
        n -= 1
        print(' ')


def pattern2():
    num = 1
    for row in range(1, 6):
        for col in range(1, row + 1):
            print(col, end=' ')

        print(' ')


def pattern3():
    n = 5
    # for row in range(1, n+1):
    #     for col in range(1, row+1):
    #         print('*', end=' ')
    #     print(' ')
    # for row in range(1, n):
    #     for col in range(n-1, 0, -1):
    #         print('*', end=' ')
    #     n -= 1
    #     print(' ')
    for row in range(0, 2 * n):
        if row > n:
            totalCol = 2 * n - row
        else:
            totalCol = row
        for col in range(0, totalCol):
            print('*', end=' ')
        print(' ')


def pattern4():
    n = 6
    for row in range(1, n):
        totalSpaces= n-row
        for space in range(1, totalSpaces):
            print(' ', end=' ')
        for col in range(1,row+1):
            print('*', end=' ')
        print(' ')

def pattern6():
    n = 5
    for row in range(0, 2*n):
        if row > n:
            totalCol = 2 * n - row
        else:
            totalCol = row
        totalSpaces = n - totalCol
        for space in range(0, totalSpaces):
            print(' ', end=' ')
        for col in range(0, totalCol):
            print(' * ', end=' ')
        print(' ')

pattern6()