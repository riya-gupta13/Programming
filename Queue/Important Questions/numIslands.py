import collections


def numIslandsDFS(grid: list[list[str]]) -> int:
    def dfs(grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != '1':
            return
        grid[i][j] = '#'
        dfs(grid, i + 1, j)
        dfs(grid, i - 1, j)
        dfs(grid, i, j + 1)
        dfs(grid, i, j - 1)

    count = 0
    if not grid:
        return 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1

    return count


def numIslandsBFS(grid: list[list[str]]) -> int:
    if not grid:
        return 0
    visit = set()
    islands = 0

    def bfs(r, c):
        q = collections.deque()
        visit.add((r, c))
        q.append((r, c))

        while q:
            row, col = q.popleft()
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                r = row + dr
                c = col + dc
                if (r in range(rows) and
                        c in range(col) and
                        grid[r][c] == "1" and
                        (r, c) not in visit):
                    q.append((r, c))
                    visit.add((r, c))

    rows = len(grid)
    cols = len(grid[0])
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r, c) not in visit:
                bfs(r, c)
                islands += 1
    return islands


grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
print(numIslands(grid))
