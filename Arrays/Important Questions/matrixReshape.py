def matrixReshape(mat: list[list[int]], r: int, c: int) -> list[list[int]]:
    flatten = []
    new_mat = []
    for row in mat:
        for num in row:
            flatten.append(num)

    if r * c != len(flatten):  # when given parameters is NOT possible and legal
        return mat
    else:
        for row_index in range(r):
            new_mat.append(flatten[row_index * c: row_index * c + c])
        return new_mat


mat = [[1, 2], [3, 4]]
r = 1
c = 4
matrixReshape(mat,r,c)
# Output: [[1, 2, 3, 4]]
