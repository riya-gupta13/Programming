def flipAndInvertImage(image: list[list[int]]):
    m = len(image)
    n = len(image[0])
    for i in range(0, m):
        image[i] = image[i][::-1]

    for i in range(0, m):
        for j in range(0, n):
            if image[i][j] == 1:
                image[i][j] = 0
            else:
                image[i][j] = 1

    print(image)


image = [[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]
flipAndInvertImage(image)
