def judgeCircle(moves: str) -> bool:
    count = 0
    counts = 0
    for i in moves:
        if i == 'U':
            count += 1
        elif i == 'D':
            count -= 1
        elif i == 'L':
            counts += 1
        else:
            counts -= 1
    if count == 0 and counts == 0:
        print("true")
    else:
        print("false")


moves = "UULLDDRR"
# Output: true
judgeCircle(moves)
