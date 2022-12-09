# https://practice.geeksforgeeks.org/problems/the-celebrity-problem/1
def celebrity(M, n):
    stack = []
    for i in range(n):
        stack.append(i)
    while len(stack) >= 2:
        i = stack.pop()
        j = stack.pop()
        if M[i][j] == 1:
            # means i knows j---> i cannot be a celebrity
            stack.append(j)
        else:
            # if i doesnt knows j--> j cannot be celebrity as everyone should know j if he's celebrity
            stack.append(i)
    # now we get a potential answer but it's not the answer as we have checked that who are nor celebrities
    # but we are not sure if the element present in stack is celebrity so fot that we will go in matrix and chk its
    # row and col if in row all 0 and col all 1 except itself
    pot = stack.pop()
    for i in range(n):
        if i != pot:
            if M[pot][i] == 1 or M[i][pot] == 0:
                return -1
    return pot
