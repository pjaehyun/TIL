class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        answer = 0
        def dfs(x, y, gold):
            nonlocal answer
            answer = max(answer, gold)
            for nx, ny in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != 0 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    dfs(nx, ny, gold + grid[nx][ny])
                    visited[nx][ny] = False
        
        visited = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] != 0:
                    visited[i][j] = True
                    dfs(i, j, grid[i][j])
                    visited[i][j] = False
        return answer