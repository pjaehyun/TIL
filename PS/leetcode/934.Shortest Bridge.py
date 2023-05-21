class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        def dfs(x, y):
            for xx, yy in [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]:
                if 0 <= xx < n and 0 <= yy < n and grid[xx][yy] == 1:
                    grid[xx][yy] = 2
                    dfs(xx, yy)

        n = len(grid)
        check = False
        dq = deque()
        visited = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    if not check:
                        check = True
                        grid[i][j] = 2
                        dfs(i, j)
                    else:
                        dq.append((i, j, 0))
                        visited[i][j] = True
        while dq:
            x, y, dist = dq.popleft()
            if grid[x][y] == 2:
                return dist - 1
            
            for xx, yy in [[x+1,y],[x,y+1],[x-1,y],[x,y-1]]:
                if 0 <= xx < n and 0 <= yy < n and grid[xx][yy] != 1 and not visited[xx][yy]:
                    visited[xx][yy] = True
                    dq.append((xx, yy, dist+1))