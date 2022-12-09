def countNegatives(grid: list[list[int]]) -> int:
    count=0
    for i in range(0,len(grid)):
        for j in grid[i]:
            if j<0:
                count+=1
    print(count)



grid = [[3,2],[1,0]]
# Output: 8
countNegatives(grid)