def finalValueAfterOperations(operations: list[str]):
    X = 0
    for x in operations:
        if x == '--X':
            X = X - 1
        elif x == 'X++':
            X = X + 1
        elif x == '++X':
            X = X + 1
        else:
            X = X - 1
    print(X)
    return X


operations = ["X++","++X","--X","X--"]
finalValueAfterOperations(operations)
