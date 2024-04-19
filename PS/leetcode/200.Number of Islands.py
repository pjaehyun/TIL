class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            for nx, ny in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
                if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and grid[nx][ny] == "1":
                    visited[nx][ny] = True
                    dfs(nx, ny)
        
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        answer = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not visited[i][j]:
                    answer += 1
                    visited[i][j] = True
                    dfs(i, j)
        return answer