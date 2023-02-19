# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
# ans = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
# print(ans)

# How do you use list comprehension to create a new list that contains the elements from two separate lists,
# in alternating order?
l1 = [1, 2, 3]
l2 = [4, 5, 6]

l = [x for pair in zip(l1, l2) for x in pair]
print(l)

# How do you use list comprehension to create a new list that contains the elements from a given list, in reverse order?
li = [x for x in l[::-1]]
print(li)

matrix = [[1, 2, 3], [4, 5, 6]]
result = [[x // 2 for x in row] for row in matrix]
print(result)

# matrix=[[0 for _ in range(3)]for _ in range(3)]
# print(matrix)
