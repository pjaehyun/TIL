class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        answer = 0
        def dfs(x, y):
            nonlocal answer
            sq = 4
            for nx, ny in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1:
                    sq -= 1
            answer += sq

            for nx, ny in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)]:
                if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    dfs(nx, ny)
                

        visited = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and not visited[i][j]:
                    visited[i][j] = True
                    dfs(i, j)
        return answer